from flask import Flask
from .site import auth
from .cliente import cliente
from .administrativo import administrativo
from .administrador import administrador
from .productos import Productos
from .site import error_handler
import logging

LOG_FILENAME = './logs.log'

def create_app():
    app = Flask(__name__)

    # registro blueprint
    app.register_blueprint(auth)
    app.register_blueprint(cliente)
    app.register_blueprint(administrativo)
    app.register_blueprint(administrador)
    app.register_blueprint(Productos)
    # error hanlder
    app.register_error_handler(401, error_handler.status_401)
    app.register_error_handler(404, error_handler.status_404)

    
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    app.logger.debug(' Se inicia correctamente aplicación')
    app.secret_key = 'my_secret_key'

    return app
