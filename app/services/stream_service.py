"""Serviço de stream.

Módulo responsável pelo gerenciamento avançado do stream,
incluindo cache, buffering e análise de performance.
"""

from typing import Optional, Callable
from app.utils.logger import get_logger

logger = get_logger(__name__)


class StreamService:
    """Serviço para gerenciar o stream de vídeo.

    Responsável por otimização de stream, cache e monitoring.
    """

    def __init__(self, buffer_size: int = 5):
        """Inicializa o serviço de stream.

        Args:
            buffer_size (int): Tamanho do buffer em frames.
        """
        self.buffer_size = buffer_size
        self.callbacks = []
        logger.info(f'StreamService inicializado com buffer_size={buffer_size}')

    def add_callback(self, callback: Callable):
        """Adiciona um callback para processar frames.

        Args:
            callback: Função a ser chamada para cada frame.
        """
        self.callbacks.append(callback)
        logger.debug(f'Callback adicionado: {callback.__name__}')

    def remove_callback(self, callback: Callable):
        """Remove um callback.

        Args:
            callback: Função a ser removida.
        """
        if callback in self.callbacks:
            self.callbacks.remove(callback)
            logger.debug(f'Callback removido: {callback.__name__}')

    def notify_callbacks(self, frame_data: bytes):
        """Notifica todos os callbacks com dados do frame.

        Args:
            frame_data (bytes): Dados do frame.
        """
        for callback in self.callbacks:
            try:
                callback(frame_data)
            except Exception as e:
                logger.error(f'Erro ao chamar callback {callback.__name__}: {str(e)}')
