"""Serviço de câmera.

Módulo responsável pela lógica de negócio relacionada
à câmera, incluindo conexão, detecção de endpoint e stream.
"""

import requests
from datetime import datetime
from typing import Optional, Generator
from flask import current_app
from app.models.camera import Camera
from app.models.stream import StreamInfo
from app.utils.logger import get_logger

logger = get_logger(__name__)


class CameraService:
    """Serviço para gerenciar a câmera IP.

    Responsável por detectar o endpoint correto da câmera,
    estabelecer conexão e fornecer o stream.
    """

    def __init__(self):
        """Inicializa o serviço de câmera."""
        self.camera: Optional[Camera] = None
        self.stream_info = StreamInfo()

    def detect_camera_endpoint(self) -> Optional[str]:
        """Detecta o endpoint correto da câmera.

        Tenta cada endpoint configurado até encontrar um que responda.

        Returns:
            str: Endpoint detectado, ou None se nenhum funcionar.
        """
        camera_ip = current_app.config['CAMERA_IP']
        camera_port = current_app.config['CAMERA_PORT']
        endpoints = current_app.config['CAMERA_ENDPOINTS']
        timeout = current_app.config['STREAM_CONNECT_TIMEOUT']

        logger.info(f'Detectando câmera em {camera_ip}:{camera_port}')

        for endpoint in endpoints:
            try:
                url = f'http://{camera_ip}:{camera_port}{endpoint}'
                logger.debug(f'Testando endpoint: {url}')

                response = requests.head(url, timeout=timeout)

                if response.status_code == 200:
                    logger.info(f'Câmera detectada no endpoint: {endpoint}')
                    self._create_camera(camera_ip, camera_port, endpoint)
                    return endpoint

            except requests.RequestException as e:
                logger.debug(f'Endpoint {endpoint} falhou: {str(e)}')
                continue

        logger.warning('Nenhum endpoint de câmera foi encontrado')
        return None

    def _create_camera(self, ip: str, port: int, endpoint: str):
        """Cria e configura o objeto de câmera.

        Args:
            ip (str): Endereço IP da câmera.
            port (int): Porta da câmera.
            endpoint (str): Endpoint do stream.
        """
        self.camera = Camera(ip=ip, port=port, endpoint=endpoint)
        self.camera.mark_connected()
        logger.info(f'Câmera criada: {self.camera.url}')

    def get_stream(self) -> Generator:
        """Obtém o stream de vídeo da câmera.

        Returns:
            Generator: Stream de bytes do vídeo.
        """
        if not self.camera:
            endpoint = self.detect_camera_endpoint()
            if not endpoint:
                raise Exception('Câmera não detectada')

        try:
            timeout = current_app.config['STREAM_READ_TIMEOUT']
            response = requests.get(
                self.camera.url,
                stream=True,
                timeout=timeout
            )
            response.raise_for_status()

            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    self.stream_info.record_frame(len(chunk))
                    yield chunk

        except requests.RequestException as e:
            logger.error(f'Erro ao obter stream: {str(e)}')
            self.camera.mark_disconnected()
            raise

    def get_camera_status(self) -> dict:
        """Retorna o status atual da câmera.

        Returns:
            dict: Status e informações da câmera.
        """
        if not self.camera:
            return {
                'connected': False,
                'message': 'Câmera não conectada',
            }

        return {
            'camera': self.camera.to_dict(),
            'stream': self.stream_info.to_dict(),
        }

    def reconnect(self) -> bool:
        """Reconecta à câmera.

        Returns:
            bool: True se reconexão bem-sucedida, False caso contrário.
        """
        logger.info('Reconectando à câmera')
        self.camera = None
        self.stream_info = StreamInfo()
        endpoint = self.detect_camera_endpoint()
        return endpoint is not None
