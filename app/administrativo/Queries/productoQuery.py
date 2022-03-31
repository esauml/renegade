from ...bd import obtener_conexion


class Producto():

    def consultarListaProductos(self, tipo_usuario):
        try:
            query = 'SELECT * FROM producto'
            conexion = obtener_conexion(tipo_usuario)
            productos = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                productos = cursor.fetchall()

            cursor.close()
            return productos
        except Exception as ex:
            raise Exception(ex)

    def consultarProducto(self, tipo_usuario, producto_id):
        try:
            query = 'SELECT * FROM producto WHERE id={}'.format(producto_id)
            conexion = obtener_conexion(tipo_usuario)
            productos = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                productos = cursor.fetchall()

            cursor.close()
            return productos
        except Exception as ex:
            raise Exception(ex)

    def actualizarUsuario(self, nombre, apellidos, email, password, id, tipo_usuario):
        try:
            query = 'UPDATE usuario SET nombres = %s, apellidos = %s, correo = %s, password=%s WHERE id = %s;'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, apellidos, email, password, id))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def eliminar_producto(self, tipo_usuario, id):
        try:
            query = 'UPDATE usuario SET activo = 0 WHERE id = %s'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def calcular_cantidad_disponible_por_producto(self, producto_id):
        # TODO Calculo de materia prima por producto
        return 0
