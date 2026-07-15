"""Pacote principal da aplicação FilterCam.

Inicializa a aplicação Flask com todas as configurações,
blueprints e extensões necessárias.
"""

from flask import Flask
from config import get_config


def create_app(config=None):
    """Factory function para criar a aplicação Flask.

    Args:
        config: Objeto de configuração. Se None, usa a configuração
                apropriada para o ambiente.

    Returns:
        Flask: Instância da aplicação Flask configurada.
    """
    app = Flask(__name__, static_folder='static', template_folder='templates')

    # Carregar configuração
    if config is None:
        config = get_config()

    app.config.from_object(config)

    # Registrar blueprints
    _register_blueprints(app)

    # Registrar context processors
    _register_context_processors(app)

    # Registrar error handlers
    _register_error_handlers(app)

    return app


def _register_blueprints(app):
    """Registra todos os blueprints da aplicação.

    Args:
        app: Instância da aplicação Flask.
    """
    from app.routes.camera_routes import camera_bp
    from app.routes.api_routes import api_bp

    app.register_blueprint(camera_bp)
    app.register_blueprint(api_bp, url_prefix='/api')


def _register_context_processors(app):
    """Registra context processors para templates.

    Args:
        app: Instância da aplicação Flask.
    """
    @app.context_processor
    def inject_config():
        """Injeta configurações nos templates."""
        return {
            'app_name': 'FilterCam',
            'app_version': '1.0.0',
        }


def _register_error_handlers(app):
    """Registra error handlers globais.

    Args:
        app: Instância da aplicação Flask.
    """
    @app.errorhandler(404)
    def not_found(error):
        """Handler para erro 404."""
        return {'error': 'Página não encontrada'}, 404

    @app.errorhandler(500)
    def internal_error(error):
        """Handler para erro 500."""
        return {'error': 'Erro interno do servidor'}, 500
