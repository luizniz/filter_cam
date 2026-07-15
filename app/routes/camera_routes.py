"""Rotas principais da câmera.

Módulo responsável pelas rotas principais que servem
a interface da aplicação e o stream de vídeo.
"""

from flask import Blueprint, render_template, current_app
from app.services.camera_service import CameraService
from app.utils.logger import get_logger

logger = get_logger(__name__)

camera_bp = Blueprint(
    'camera',
    __name__,
    template_folder='../templates',
    static_folder='../../static'
)


@camera_bp.route('/', methods=['GET'])
def index():
    """Serve a página principal da aplicação.

    Returns:
        str: HTML renderizado da página principal.
    """
    logger.info('Servindo página principal')
    return render_template('index.html')


@camera_bp.route('/stream', methods=['GET'])
def video_stream():
    """Retorna o stream de vídeo da câmera.

    Returns:
        Response: Stream MJPEG da câmera.
    """
    try:
        logger.info('Iniciando stream de vídeo')
        camera_service = CameraService()
        return camera_service.get_stream()
    except Exception as e:
        logger.error(f'Erro ao obter stream: {str(e)}')
        return {'error': 'Não foi possível conectar ao stream'}, 500
