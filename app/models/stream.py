"""Modelo de stream de vídeo.

Classe que gerencia o estado do stream de vídeo.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class StreamInfo:
    """Informações do stream de vídeo.

    Attributes:
        frames_received (int): Total de frames recebidos.
        frames_dropped (int): Total de frames perdidos.
        bytes_received (int): Total de bytes recebidos.
        avg_latency (float): Latência média em ms.
        current_fps (float): FPS atual.
        start_time (datetime): Hora de início do stream.
        last_frame_time (datetime): Hora do último frame.
    """

    frames_received: int = 0
    frames_dropped: int = 0
    bytes_received: int = 0
    avg_latency: float = 0.0
    current_fps: float = 0.0
    start_time: datetime = field(default_factory=datetime.now)
    last_frame_time: Optional[datetime] = None

    @property
    def uptime(self) -> float:
        """Retorna o tempo de atividade em segundos.

        Returns:
            float: Tempo em segundos.
        """
        return (datetime.now() - self.start_time).total_seconds()

    @property
    def total_frames(self) -> int:
        """Retorna o total de frames processados.

        Returns:
            int: Total de frames.
        """
        return self.frames_received + self.frames_dropped

    def record_frame(self, bytes_count: int = 0):
        """Registra um novo frame recebido.

        Args:
            bytes_count (int): Número de bytes do frame.
        """
        self.frames_received += 1
        self.bytes_received += bytes_count
        self.last_frame_time = datetime.now()

    def record_dropped_frame(self):
        """Registra um frame perdido."""
        self.frames_dropped += 1

    def to_dict(self) -> dict:
        """Converte o modelo para dicionário.

        Returns:
            dict: Representação em dicionário do modelo.
        """
        return {
            'frames_received': self.frames_received,
            'frames_dropped': self.frames_dropped,
            'bytes_received': self.bytes_received,
            'avg_latency': self.avg_latency,
            'current_fps': self.current_fps,
            'uptime': self.uptime,
            'total_frames': self.total_frames,
        }
