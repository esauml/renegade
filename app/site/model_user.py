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

    @classmethod
    def login(self, db, user):
        try:
            return self.consultar_por_email(USUARIO_ADMIN, user.email)
        except Exception as ex:
            raise Exception(ex)

    def registro_usuario(self, tipo_usuario, nombre, apellidos, email, password):
        try:
            query = 'INSERT INTO Usuario(nombres, apellidos, correo, password, active) VALUES (%s, %s, %s, %s, 1)'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, apellidos, email,
                               generate_password_hash(password, method='sha256')))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def consultar_cliente_por_id(tipo_usuario, id):
        try:
            query = 'SELECT * FROM Usuario WHERE id = %s'
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

    def consultar_por_email(self, email):
        try:
            query = "SELECT id, nombres, apellidos, correo, password, active FROM Usuario WHERE correo = %s"
            conexion = obtener_conexion(USUARIO_ADMIN)

            with conexion.cursor() as cursor:
                cursor.execute(query, (email))
                consulta = cursor.fetchone()
                cursor.close()

            if consulta != None:
                from .Usuario import Usuario
                return Usuario(consulta[0], consulta[1], consulta[2], consulta[3], consulta[4], consulta[5])

            return None
        except Exception as ex:
            raise Exception(ex)
