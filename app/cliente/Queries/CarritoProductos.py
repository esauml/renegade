

from itertools import product
from math import prod
from app.bd import obtener_conexion


class QueriesCarrito():

    def carrito_usuario(self, USER_TYPE, id_usuario):
        try:
            query_carrito = 'SELECT * FROM Carrito where idUsuario=%s and status=1'
            
            conexion = obtener_conexion(USER_TYPE)
            carrito = []
            productos_carrito = []
            

            with conexion.cursor() as cursor:
                # carrito
                cursor.execute(query_carrito, (id_usuario,))
                carrito = cursor.fetchall()
                
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
    
    def agregar_producto(self, USER_TYPE, id_user, id_producto, cantidad)