"""Decoradores customizados.

Módulo com decoradores úteis para a aplicação.
"""

from functools import wraps
from flask import jsonify
from app.utils.logger import get_logger

logger = get_logger(__name__)


def handle_errors(f):
    """Decorador para tratamento de erros em rotas.

    Captura exceções e retorna respostas JSON apropriadas.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.error(f'Erro não tratado em {f.__name__}: {str(e)}')
            return jsonify({'error': 'Erro interno do servidor'}), 500

    return decorated_function


def require_camera_connection(f):
    """Decorador para verificar se a câmera está conectada."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        from app.services.camera_service import CameraService
        camera_service = CameraService()

        if not camera_service.camera or not camera_service.camera.connected:
            logger.warning('Tentativa de acesso com câmera desconectada')
            return jsonify({'error': 'Câmera não conectada'}), 503

        return f(*args, **kwargs)

    return decorated_function
