from ..bd import obtener_conexion

class Producto():

    def consultar_productos(self, tipo_usuario):
        try:
            query = 'SELECT id, nombre, descripcion, precio, activo FROM producto'
            conexion = obtener_conexion(tipo_usuario)
            productos = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                productos = cursor.fetchall()

            cursor.close()
            return productos
        except Exception as ex:
            raise Exception(ex)

    def consultar_producto_por_id(self, tipo_usuario, id):
        try:
            query = 'SELECT prod.id, prod.nombre, descripcion, precio, activo, mp.nombre, pmp.cantidad \
                    FROM producto prod \
                        INNER JOIN producto_materia_prima pmp ON prod.id = pmp.producto_id \
                        INNER JOIN materia_prima mp on pmp.mataria_prima_id = mp.id \
                    WHERE prod.id = %s'
            conexion = obtener_conexion(tipo_usuario)
            producto = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                producto = cursor.fetchone()

            cursor.close()
            # TODO self.calcular_cantidad_disponible_por_producto(producto[0]).
            return producto
        except Exception as ex:
            raise Exception(ex)

    def actualizar_producto(self, tipo_usuario, nombre, descripcion, precio, id):
        try:
            query = 'UPDATE producto SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s;'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, descripcion, precio, id))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def eliminar_producto(self, tipo_usuario, id):
        try:
            query = 'UPDATE producto SET activo = 0 WHERE id = %s'
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