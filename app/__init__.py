from flask import Flask
from flask_security import Security
# from flask_wtf.csrf import CSRFProtect

from .site import auth, model_user
from flask_mysqldb import MySQL
from .cliente import cliente
from .administrativo import administrativo
from .administrador import administrador
from flask_login import LoginManager
from .site import error_handler


def create_app():
    app = Flask(__name__)

    # registro blueprint
    app.register_blueprint(auth)
    app.register_blueprint(cliente)
    app.register_blueprint(administrativo)
    app.register_blueprint(administrador)

    #error hanlder
    app.register_error_handler(401, error_handler.status_401)
    app.register_error_handler(404, error_handler.status_404)

    app.secret_key = 'my_secret_key'

    #Registro de flask login
    login_manager_app = LoginManager(app)


    @login_manager_app.user_loader
    def user_loader(id):
        return model_user.ModelUser.get_by_id(id)
    
    return app