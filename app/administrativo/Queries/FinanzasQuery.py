from ...bd import obtener_conexion
from ...config import USUARIO_ADMINISTATIVO as USER_TYPE


class QueriesFinanzas():
    
    def ganancia_anual():
        try:
            return 0
            
        except Exception as e:
            raise Exception(e)
    
    def ganancia_mes_actual():
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
                cursor.execute(query, (id,))
                ganancia_anual = cursor.fetchall()

            cursor.close()
            return ganancia_anual
            
        except Exception as e:
            raise Exception(e)

    def ganancia_meses_anio():
        return 0
    
    def top_10_productos_vendidos():
        return 0    