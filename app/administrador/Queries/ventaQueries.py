from ...bd import obtener_conexion
from ...config import USUARIO_ADMIN, USUARIO_CLIENTE
from werkzeug.security import generate_password_hash


class Venta:

    def consultar_ventas(self):
        try:
            query = 'select * from venta;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            ventas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                ventas = cursor.fetchall()

            cursor.close()
            return ventas
        except Exception as ex:
            raise Exception(ex)

