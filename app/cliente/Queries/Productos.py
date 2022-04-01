from ...bd import obtener_conexion

class QueriesProducto():

    def consultar_productos(self, USER_TYPE):
        try:
            query = 'SELECT * FROM producto where stock > 0;'
            conexion = obtener_conexion(USER_TYPE)
            productos = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                productos = cursor.fetchall()

            cursor.close()
            return productos
        except Exception as ex:
            raise Exception(ex)

    def consultar_productos_busqueda(self, USER_TYPE, criteria):
        try:
            query = "SELECT * from producto where nombre LIKE '%" + criteria +" %' or descripcion LIKE '%" + criteria + "%'"
            conexion = obtener_conexion(USER_TYPE)
            productos = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                productos = cursor.fetchall()

            cursor.close()
            return productos
        except Exception as ex:
            raise Exception(ex)

    def consultar_producto_por_id(self, USER_TYPE, id):
        try:
            query = 'SELECT * from producto where id=%s'
            conexion = obtener_conexion(USER_TYPE)
            producto = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                producto = cursor.fetchone()

            cursor.close()
            return producto
        except Exception as ex:
            raise Exception(ex)


