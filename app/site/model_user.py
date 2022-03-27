from . import User
from ..bd import obtener_conexion
from ..config import USUARIO_ADMIN
from werkzeug.security import generate_password_hash


class ModelUser():

    @classmethod
    def get_by_id(self, id):
        try:
            return self.consultar_cliente_por_id(USUARIO_ADMIN, id)
        except Exception as ex:
            raise Exception(ex)

    def registro_usuario(self, tipo_usuario, nombre, apellidos, email, password):
        try:
            query = 'INSERT INTO usuario(username, password, email, name, lastname) VALUES (%s, %s, %s, %s, %s)'

            conexion = obtener_conexion(tipo_usuario)
            with conexion.cursor() as cursor:
                cursor.execute(query, (email, generate_password_hash(password, method='sha256'),email, nombre, apellidos))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def consultar_cliente_por_email(self, tipo_usuario, email):
        try:
            query = 'SELECT id FROM usuario WHERE email = %s'
            conexion = obtener_conexion(tipo_usuario)
            usuario = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (email))
                usuario = cursor.fetchone()

            cursor.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)

    def consultar_cliente_por_id(tipo_usuario, id):
        try:
            query = 'SELECT * FROM usuario WHERE id = %s'
            conexion = obtener_conexion(tipo_usuario)
            usuario = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id))
                usuario = cursor.fetchone()
                cursor.close()

                if usuario != None:
                    return usuario

            return None
        except Exception as ex:
            raise Exception(ex)

    def consultar_por_email(self, tipo_usuario, email):
        try:
            query = "SELECT id, username, password, email, name, lastname FROM usuario WHERE email = %s"
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (email,))
                consulta = cursor.fetchone()
                cursor.close()

            if consulta != None:
                return User(consulta[0], consulta[1], consulta[2], consulta[3], consulta[4], consulta[5])

            return None
        except Exception as ex:
            raise Exception(ex)
