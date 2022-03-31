from werkzeug.security import check_password_hash
from flask_login import UserMixin


class Usuario(UserMixin):

    def __init__(self, id, nombre, apellidos, email, password, activo, idRol) -> None:
        self.id = id
        self.password = password
        self.email = email
        self.nombre = nombre
        self.apellidos = apellidos
        self.activo = activo
        self.idRol = idRol

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
