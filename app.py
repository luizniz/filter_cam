#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Ponto de entrada da aplicação FilterCam.

Arquivo principal que inicializa e executa a aplicação Flask.
Execute com: python app.py
"""

import os
import sys
from app import create_app
from app.utils.logger import get_logger

# Configurar o diretório de trabalho
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

logger = get_logger(__name__)


def main():
    """Função principal que cria e executa a aplicação."""
    try:
        # Criar aplicação
        app = create_app()
        logger.info('Aplicação FilterCam criada com sucesso')
        logger.info(f'Ambiente: {app.config["DEBUG"]}')

        # Configurações de desenvolvimento
        if app.config['DEBUG']:
            logger.info('Modo DEBUG ativado')
            app.run(
                host='0.0.0.0',
                port=5000,
                debug=True,
                use_reloader=True
            )
        else:
            # Configurações de produção
            logger.info('Modo PRODUÇÃO ativado')
            app.run(
                host='0.0.0.0',
                port=5000,
                debug=False
            )

    except Exception as e:
        logger.critical(f'Erro ao iniciar a aplicação: {str(e)}')
        sys.exit(1)


if __name__ == '__main__':
    main()
