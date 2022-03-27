from flask import Flask
# from flask_wtf.csrf import CSRFProtect

from .site import auth
from .cliente import cliente
from .administrativo import administrativo
from .administrador import administrador

def create_app():
    app = Flask(__name__)

    # registro blueprint
    app.register_blueprint(auth)
    app.register_blueprint(cliente)
    app.register_blueprint(administrativo)
    app.register_blueprint(administrador)

    app.secret_key = 'my_secret_key'
    #CSRFProtect(app)
    return app