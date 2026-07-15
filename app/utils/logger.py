"""Sistema de logging.

Módulo centralizado para configuração e gerenciamento de logs.
"""

import logging
import logging.handlers
from flask import current_app


def get_logger(name: str) -> logging.Logger:
    """Obtém ou cria um logger.

    Args:
        name (str): Nome do logger (geralmente __name__).

    Returns:
        logging.Logger: Instância do logger configurada.
    """
    logger = logging.getLogger(name)

    # Evitar duplicação de handlers
    if logger.handlers:
        return logger

    # Configurar nível de log
    try:
        log_level = current_app.config.get('LOG_LEVEL', 'INFO')
    except RuntimeError:
        log_level = 'INFO'

    logger.setLevel(getattr(logging, log_level))

    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, log_level))

    # Formato
    try:
        log_format = current_app.config.get('LOG_FORMAT')
    except RuntimeError:
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    formatter = logging.Formatter(log_format)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger
