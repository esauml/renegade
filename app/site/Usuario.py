from ..bd import obtener_conexion
from werkzeug.security import generate_password_hash
from flask_security import UserMixin


class Usuario(UserMixin):

    # TODO Problema con autenticación flask.
    # def __init__(self, is_authenticated, is_active, is_anonymous):
    #    self.is_authenticated = is_authenticated
    #    self.is_active = is_active
    #    self.is_anonymous = is_anonymous

    def registro_usuario(self, tipo_usuario, nombre, apellidos, email, password):
        query = 'INSERT INTO usuario(nombre, apellidos, email, password, activo) \
        VALUES (%s, %s, %s, %s, 1)'

        conexion = obtener_conexion(tipo_usuario)
        with conexion.cursor() as cursor:
            cursor.execute(query, (nombre, apellidos, email,
                           generate_password_hash(password, method='sha256')))

        conexion.commit()
        cursor.close()

    def consultar_cliente_por_email(self, tipo_usuario, email):
        query = 'SELECT id FROM usuario WHERE email = %s'
        conexion = obtener_conexion(tipo_usuario)
        usuario = None

        with conexion.cursor() as cursor:
            cursor.execute(query, (id,))
            usuario = cursor.fetchone()

        cursor.close()
        return usuario

    def consultar_por_email(self, tipo_usuario, email):
        query = "SELECT * FROM usuario WHERE email = %s"
        conexion = obtener_conexion(tipo_usuario)
        usuario = None

        with conexion.cursor() as cursor:
            cursor.execute(query, (email,))
            usuario = cursor.fetchone()

        cursor.close()
        return usuario
