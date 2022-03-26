from flask import Flask
# from flask_wtf.csrf import CSRFProtect
from .site import auth
from .cliente import cliente
from .administrativo import administrativo


def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth)
    app.register_blueprint(cliente)
    app.register_blueprint(administrativo)

    app.secret_key = 'my_secret_key'
    #CSRFProtect(app)
    return app