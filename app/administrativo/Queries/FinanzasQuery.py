from ...bd import obtener_conexion
from ...config import USUARIO_ADMINISTATIVO as USER_TYPE


class QueriesFinanzas():
    
    def ganancia_anual(self):
        try:
            query = '\
                select ifnull(sum(precio), 0) from ProductoCarrito where idCarrito in (\
                    select id from carrito where id in (\
                        select idCarrito from Venta where year(fecha) = year(now())\
                    )\
                );'
            conexion = obtener_conexion(USER_TYPE)
            ganancia_anual = 0

            with conexion.cursor() as cursor:
                cursor.execute(query)
                ganancia_anual = cursor.fetchall()

            cursor.close()
            return ganancia_anual
            
        except Exception as e:
            raise Exception(e)
    
    def ganancia_mes_actual(self):
        try:
            query = '\
                select ifnull(sum(precio), 0) from ProductoCarrito where idCarrito in (\
                    select id from carrito where id in (\
                        select idCarrito from Venta where month(fecha) = month(NOW()) and year(fecha) = year(now())\
                    )\
                );'
            conexion = obtener_conexion(USER_TYPE)
            ganancia_anual = 0

            with conexion.cursor() as cursor:
                cursor.execute(query)
                ganancia_anual = cursor.fetchall()

            cursor.close()
            return ganancia_anual
            
        except Exception as e:
            raise Exception(e)

    def ganancia_meses_anio(self):
        try:
            query = '\
                select Month(fecha) index_meses, \
                    (select ifnull(sum(precio), 0) from ProductoCarrito where idCarrito in (\
                        select id from carrito where id in (\
                            select idCarrito from Venta where month(fecha) = index_meses and year(fecha) = year(now())\
                        )\
                    )) ventas\
                from Venta where year(fecha) = year(now()) group by index_meses;'
            conexion = obtener_conexion(USER_TYPE)
            ganancia_anual = 0

            with conexion.cursor() as cursor:
                cursor.execute(query)
                ganancia_anual = cursor.fetchall()

            cursor.close()
            return ganancia_anual
            
        except Exception as e:
            raise Exception(e)
    
    def top_10_productos_vendidos(self):
        try:
            query = '\
                select idProducto, \
                    (select nombre from Producto where id = IdProducto), \
                    sum(precio) \
                from ProductoCarrito where idCarrito in (\
                    select id from carrito where id in (\
                        select idCarrito from Venta\
                    )\
                ) group by idProducto;'
            conexion = obtener_conexion(USER_TYPE)
            ganancia_anual = 0

            with conexion.cursor() as cursor:
                cursor.execute(query)
                ganancia_anual = cursor.fetchall()

            cursor.close()
            return ganancia_anual
            
        except Exception as e:
            raise Exception(e)  