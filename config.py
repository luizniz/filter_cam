"""Configuração da aplicação FilterCam.

Módulo responsável por carregar e validar todas as configurações
da aplicação, incluindo variáveis de ambiente e constantes globais.
"""

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()


class Config:
    """Configurações base da aplicação."""

    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('FLASK_DEBUG', 'False') == 'True'
    TESTING = False

    # Câmera
    CAMERA_IP = os.getenv('CAMERA_IP', '192.168.0.80')
    CAMERA_PORT = int(os.getenv('CAMERA_PORT', '4747'))

    # URLs de teste para endpoints da câmera
    CAMERA_ENDPOINTS = [
        '/video',
        '/video.mjpg',
        '/videofeed',
        '/mjpeg',
        '/shot.jpg',
        '/stream',
        '/cgi-bin/mjpg_streamer',
    ]

    # Configurações de timeout
    STREAM_CONNECT_TIMEOUT = 5  # segundos
    STREAM_READ_TIMEOUT = 10    # segundos

    # Configurações de cache
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300

    # Configurações de logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


class DevelopmentConfig(Config):
    """Configurações para ambiente de desenvolvimento."""

    DEBUG = True
    LOG_LEVEL = 'DEBUG'


class ProductionConfig(Config):
    """Configurações para ambiente de produção."""

    DEBUG = False
    LOG_LEVEL = 'INFO'


class TestingConfig(Config):
    """Configurações para testes."""

    TESTING = True
    DEBUG = True
    LOG_LEVEL = 'DEBUG'


def get_config():
    """Retorna a configuração apropriada baseada no ambiente.

    Returns:
        Config: Configuração para o ambiente atual.
    """
    env = os.getenv('FLASK_ENV', 'development').lower()

    config_map = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig,
    }

    return config_map.get(env, DevelopmentConfig)
