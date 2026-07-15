"""Rotas de API da aplicação.

Módulo responsável pelas rotas de API que fornecem
informações e controle sobre o sistema.
"""

from flask import Blueprint, jsonify, request
from app.services.camera_service import CameraService
from app.utils.logger import get_logger

logger = get_logger(__name__)

api_bp = Blueprint('api', __name__)


@api_bp.route('/camera/status', methods=['GET'])
def camera_status():
    """Retorna o status atual da câmera.

    Returns:
        dict: Informações de status da câmera.
    """
    try:
        camera_service = CameraService()
        status = camera_service.get_camera_status()
        return jsonify(status), 200
    except Exception as e:
        logger.error(f'Erro ao obter status: {str(e)}')
        return jsonify({'error': 'Erro ao obter status'}), 500


@api_bp.route('/camera/detect', methods=['POST'])
def detect_camera():
    """Detecta e retorna o endpoint correto da câmera.

    Returns:
        dict: Endpoint detectado ou mensagem de erro.
    """
    try:
        camera_service = CameraService()
        endpoint = camera_service.detect_camera_endpoint()
        if endpoint:
            return jsonify({'endpoint': endpoint}), 200
        return jsonify({'error': 'Câmera não encontrada'}), 404
    except Exception as e:
        logger.error(f'Erro ao detectar câmera: {str(e)}')
        return jsonify({'error': 'Erro ao detectar câmera'}), 500


@api_bp.route('/camera/reconnect', methods=['POST'])
def reconnect_camera():
    """Reconecta à câmera.

    Returns:
        dict: Resultado da reconexão.
    """
    try:
        camera_service = CameraService()
        result = camera_service.reconnect()
        if result:
            return jsonify({'message': 'Reconectado com sucesso'}), 200
        return jsonify({'error': 'Falha ao reconectar'}), 500
    except Exception as e:
        logger.error(f'Erro ao reconectar: {str(e)}')
        return jsonify({'error': 'Erro ao reconectar'}), 500


@api_bp.route('/health', methods=['GET'])
def health_check():
    """Verifica a saúde da aplicação.

    Returns:
        dict: Status de saúde.
    """
    return jsonify({
        'status': 'ok',
        'service': 'filtercam',
        'version': '1.0.0'
    }), 200
