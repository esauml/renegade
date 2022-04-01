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
            producto = None

            with conexion.cursor() as cursor:
                cursor.execute(query)
                producto = cursor.fetchone()

            cursor.close()
            return producto
        except Exception as ex:
            raise Exception(ex)

    def actualizarProducto(self, nombre, apellidos, email, password, id, tipo_usuario):
        try:
            query = 'UPDATE usuario SET nombres = %s, apellidos = %s, correo = %s, password=%s WHERE id = %s;'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, apellidos, email, password, id))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def agregarProducto(self, nombre, descripcion, talla, tipo_usuario):
        try:
            query = 'UPDATE Producto SET nombre = %s, descripcion = %s, talla = %s;'

            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, descripcion, talla))

            conexion.commit()
            cursor.close()
            return "Agregado"
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
