"""Modelo de câmera.

Classe que representa uma câmera IP e suas propriedades.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Camera:
    """Representa uma câmera IP.

    Attributes:
        ip (str): Endereço IP da câmera.
        port (int): Porta da câmera.
        endpoint (str): Endpoint do stream (ex: /video, /mjpeg).
        resolution (tuple): Resolução do vídeo (largura, altura).
        fps (float): Frames por segundo estimado.
        connected (bool): Estado da conexão.
        connected_at (datetime): Data/hora de conexão.
        last_frame_time (datetime): Última atualização de frame.
    """

    ip: str
    port: int
    endpoint: Optional[str] = None
    resolution: tuple = field(default_factory=lambda: (0, 0))
    fps: float = 0.0
    connected: bool = False
    connected_at: Optional[datetime] = None
    last_frame_time: Optional[datetime] = None

    @property
    def url(self) -> str:
        """Retorna a URL completa da câmera.

        Returns:
            str: URL da câmera.
        """
        if self.endpoint:
            return f'http://{self.ip}:{self.port}{self.endpoint}'
        return f'http://{self.ip}:{self.port}'

    @property
    def connection_duration(self) -> Optional[float]:
        """Retorna o tempo de conexão em segundos.

        Returns:
            float: Tempo em segundos, ou None se não conectado.
        """
        if self.connected and self.connected_at:
            return (datetime.now() - self.connected_at).total_seconds()
        return None

    def mark_connected(self):
        """Marca a câmera como conectada."""
        self.connected = True
        self.connected_at = datetime.now()

    def mark_disconnected(self):
        """Marca a câmera como desconectada."""
        self.connected = False
        self.connected_at = None

    def to_dict(self) -> dict:
        """Converte o modelo para dicionário.

        Returns:
            dict: Representação em dicionário do modelo.
        """
        return {
            'ip': self.ip,
            'port': self.port,
            'endpoint': self.endpoint,
            'url': self.url,
            'resolution': self.resolution,
            'fps': self.fps,
            'connected': self.connected,
            'connected_at': self.connected_at.isoformat() if self.connected_at else None,
            'connection_duration': self.connection_duration,
        }
