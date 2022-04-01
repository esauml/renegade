from ...config import USUARIO_CLIENTE as USER_TYPE
from .Productos import QueriesProducto
from ...bd import obtener_conexion


class QueriesCarrito():

    def carrito_usuario(self, USER_TYPE, id_usuario):
        try:
            query_carrito = 'SELECT * FROM Carrito where idUsuario=%s and status=1;'

            conexion = obtener_conexion(USER_TYPE)
            carrito = []
            productos_carrito = []

            with conexion.cursor() as cursor:
                # carrito
                cursor.execute(query_carrito, (id_usuario,))
                carrito = cursor.fetchone()

                # productos de carrito
                query_productos_carrito = 'SELECT * \
                    FROM ProductoCarrito c \
                    inner join Producto p \
                        on c.idProducto = p.id \
                    where idCarrito = %s;);'
                cursor.execute(query_productos_carrito, (carrito[0],))
                productos_carrito = cursor.fetchall()

            cursor.close()

            # append productos_carrito into carrito
            carrito = carrito + (productos_carrito,)

            return carrito
        except Exception as ex:
            raise Exception(ex)

    def agregar_producto(self, USER_TYPE, id_user, id_producto, cantidad):
        try:
            carrito = None
            # buscar carrito
            self.buscar_carrito(USER_TYPE, id_user)
            # check if it exists
            if carrito is None:
                # insert into carrito
                carrito = self.insert_carrito(USER_TYPE, id_user)
            # check if proudcto is already in carrito
            carrito_id = carrito[0]
            is_in = self.search_proudcto_in_carrito(
                USER_TYPE, carrito_id, id_producto)

            # producto a actualizar
            precio = 0
            # buscar producto para saber precio
            producto_query = QueriesProducto()
            producto_search = producto_query.consultar_producto_por_id(
                USER_TYPE, id_producto)
            producto_precio = producto_search[3]

            if is_in is not None:
                # new cantidad
                cantidad = cantidad + int(is_in[2])
                # calulo de subtotal
                precio = int(cantidad) * int(producto_precio)
                # addition to stock
                self.update_producto_to_carrito(
                    USER_TYPE, carrito_id, id_producto, cantidad, precio)
            else:
                # calulo de subtotal
                precio = int(cantidad) * int(producto_precio)
                # add producto to carrito
                self.add_producto_to_carrito(
                    USER_TYPE, carrito_id, id_producto, cantidad, precio)

            return True
        except Exception as ex:
            raise Exception(ex)

    def buscar_carrito(self,  USER_TYPE, id_user):
        try:
            query_carrito = 'SELECT * FROM Carrito where idUsuario=%s and status=1;'

            conexion = obtener_conexion(USER_TYPE)
            carrito = None

            with conexion.cursor() as cursor:
                # carrito
                cursor.execute(query_carrito, (id_user,))
                carrito = cursor.fetchall()

            cursor.close()

            return carrito
        except Exception as ex:
            raise Exception(ex)

    def insert_carrito(self,  USER_TYPE, id_user):
        try:
            query = 'INSERT INTO Carrito(idUsuario) values(%s);'
            conexion = obtener_conexion(USER_TYPE)

            with conexion.cursor() as cursor:
                cursor.execute(query, (id_user,))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def search_proudcto_in_carrito(self,  USER_TYPE, carrito_id, producto_id):
        try:
            query_carrito = 'SELECT * FROM ProductoCarrito where idCarrito=%s and idProducto=%s;'

            conexion = obtener_conexion(USER_TYPE)
            carrito = None

            with conexion.cursor() as cursor:
                # carrito
                cursor.execute(query_carrito, (carrito_id, producto_id,))
                carrito = cursor.fetchone()

            cursor.close()

            return carrito
        except Exception as ex:
            raise Exception(ex)

    def update_producto_to_carrito(self,  USER_TYPE, carrito_id, producto_id, cantidad):
        try:
            query = 'UPDATE ProductoCarrito set cantidad=%s where idCarrito=%s and idProducto=%s;'
            conexion = obtener_conexion(USER_TYPE)

            with conexion.cursor() as cursor:
                cursor.execute(query, (cantidad, carrito_id, producto_id))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def add_producto_to_carrito(self,  USER_TYPE, carrito_id, producto_id, cantidad, precio):
        try:
            query = 'INSERT INTO ProductoCarrito(idProducto, idCarrito, cantidad, precio) \
                values(%s, %s, %s, %s);'
            conexion = obtener_conexion(USER_TYPE)

            with conexion.cursor() as cursor:
                cursor.execute(
                    query, (producto_id, carrito_id, cantidad, precio))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)
