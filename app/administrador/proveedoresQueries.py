from ..bd import obtener_conexion
from ..config import USUARIO_ADMIN

class ProveedoresQueries():

    def consultar_proveedores(self):
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

    def consultar_proveedor_por_id(self, id):
        try:
            query = 'select id, nombre, contacto, telefono, correo from proveedor where id = %s;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            proveedor = []

            with conexion.cursor() as cursor:
                cursor.execute(query, (id))
                proveedor = cursor.fetchone()

            cursor.close()
            return proveedor
        except Exception as ex:
            raise Exception(ex)

    def actualizar_proveedor(self, nombre, correo, contacto, telefono, id):
        try:
            query = 'UPDATE proveedor SET nombre = %s, correo = %s, contacto = %s, telefono = %s WHERE id = %s;'
            conexion = obtener_conexion(USUARIO_ADMIN)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, correo, contacto, telefono, id))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def consultar_materiasprimas_por_proveedor_id(self, id):
        try:
            query = 'SELECT m.nombre, m.descripcion, c2.cantidad, c2.costo FROM proveedor p \
                        INNER JOIN compra c on p.id = c.idProveedor \
                        INNER JOIN comprastockmateria c2 on c.id = c2.idOrdenCompra \
                        INNER JOIN materiaprima m on c2.idMateriaPrima = m.id \
                        WHERE p.id = %s'

            conexion = obtener_conexion(USUARIO_ADMIN)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query, (id))
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)
