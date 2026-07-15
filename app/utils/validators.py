"""Validadores de entrada.

Módulo com funções para validação de dados de entrada.
"""

import re
from typing import Optional


def is_valid_ip(ip: str) -> bool:
    """Valida se uma string é um endereço IP válido.

    Args:
        ip (str): String a validar.

    Returns:
        bool: True se IP válido, False caso contrário.
    """
    pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    if re.match(pattern, ip):
        parts = ip.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    return False


def is_valid_port(port: int) -> bool:
    """Valida se uma porta é válida.

    Args:
        port (int): Número da porta.

    Returns:
        bool: True se porta válida, False caso contrário.
    """
    return isinstance(port, int) and 1 <= port <= 65535


def is_valid_endpoint(endpoint: str) -> bool:
    """Valida se um endpoint é válido.

    Args:
        endpoint (str): Endpoint a validar.

    Returns:
        bool: True se endpoint válido, False caso contrário.
    """
    if not isinstance(endpoint, str) or not endpoint.startswith('/'):
        return False
    pattern = r'^/[a-zA-Z0-9._-]+(/[a-zA-Z0-9._-]+)*$'
    return re.match(pattern, endpoint) is not None
