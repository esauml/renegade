from ..bd import obtener_conexion
from ..config import USUARIO_ADMIN


class ProveedoresQueries():

    def consultar_proveedores():
        try:
            query = 'select id, nombre, contacto, telefono, correo from proveedor;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            proveedores = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                proveedores = cursor.fetchall()

            cursor.close()
            return proveedores
        except Exception as ex:
            raise Exception(ex)
