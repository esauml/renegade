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

    def actualizarProducto(self, producto_id, nombre, descripcion, talla, image_ur, cant_min, cant_max, tipo_usuario):
        try:
            query = 'UPDATE Producto SET nombre = %s, descripcion = %s, talla = %s, image_url = %s, cant_min = %s, cant_max = %s WHERE id = %s;'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, descripcion, talla, image_ur, cant_min, cant_max, producto_id))

            conexion.commit()
            cursor.close()
            return "El producto fue modificado"
        except Exception:
            return "El producto no pudo ser modificado"

    def agregarProducto(self, nombre, descripcion, talla, image_url, tipo_usuario):
        try:
            query = 'INSERT INTO Producto(nombre, descripcion, talla, image_url) VALUES (%s,%s,%s,%s);'

            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, descripcion, talla, image_url))

            conexion.commit()
            cursor.close()
            return "El producto fue agregado"
        except Exception:
            return "El producto no pudo ser agregado"

    def estatus_producto(self, product_id, activo, tipo_usuario):
        try:
            query = 'UPDATE Producto SET activo = %s WHERE id = %s'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (activo, product_id))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)
