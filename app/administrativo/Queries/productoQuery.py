from ...bd import obtener_conexion


class Producto():

    def consultarListaProductos(self, tipo_usuario):
        try:
            query = 'SELECT id, nombre, descripcion, precio, talla, stock, activo FROM vista_producto;'
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
            query = 'SELECT id, nombre, descripcion, precio, talla, stock, image_url, cant_min, cant_max, activo FROM vista_producto WHERE id = %s;'
            conexion = obtener_conexion(tipo_usuario)
            producto = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (producto_id,))
                producto = cursor.fetchone()

            cursor.close()
            return producto
        except Exception as ex:
            raise Exception(ex)

    def consultarMateriaPrima(self, tipo_usuario):
        try:
            query = 'SELECT id, nombre FROM materiaprima;'
            conexion = obtener_conexion(tipo_usuario)
            materias = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                materias = cursor.fetchall()

            cursor.close()
            return materias
        except Exception as ex:
            raise Exception(ex)

    def consultar_estructura_producto(self, producto_id, tipo_usuario):
        try:
            query = 'SELECT * FROM vista_estructura_materia WHERE idProducto = %s'
            conexion = obtener_conexion(tipo_usuario)
            materiaPrima = []

            with conexion.cursor() as cursor:
                cursor.execute(query, (producto_id,))
                materiaPrima = cursor.fetchall()

            cursor.close()
            return materiaPrima
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
        except Exception as ex:
            raise Exception(ex)
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
        except Exception as ex:
            raise Exception(ex)
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

    def agregar_materia_estructura(self, product_id, materia_id, cantidad, descripcion, tipo_usuario):
        try:
            query = 'INSERT INTO estructura(idProducto, idMateriaPrima, cantidad, descripcion) VALUES (%s, %s, %s, %s);'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (product_id, materia_id, cantidad, descripcion))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def eliminar_materia_estructura(self, pieza_id, tipo_usuario):
        try:
            query = 'DELETE FROM estructura WHERE id = %s;'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (pieza_id,))

            conexion.commit()
            cursor.close()
            return "Materia prima eliminada de la lista de diseño"
        except Exception as ex:
            raise Exception(ex)
            return "No se pudo eliminar la materia prima del diseño"
