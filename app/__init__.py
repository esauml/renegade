from flask import Flask
from .site import auth
from .cliente import cliente
from .administrativo import administrativo
from .administrador import administrador
from .site import error_handler


def create_app():
    app = Flask(__name__)

    # registro blueprint
    app.register_blueprint(auth)
    app.register_blueprint(cliente)
    app.register_blueprint(administrativo)
    app.register_blueprint(administrador)

    # error hanlder
    app.register_error_handler(401, error_handler.status_401)
    app.register_error_handler(404, error_handler.status_404)

    app.secret_key = 'my_secret_key'

    return app
