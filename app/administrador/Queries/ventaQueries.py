from ...bd import obtener_conexion
from ...config import USUARIO_ADMIN, USUARIO_CLIENTE
from werkzeug.security import generate_password_hash


class Venta:

    def consultar_ventas(self):
        try:
            query = 'SELECT * FROM venta;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            ventas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                ventas = cursor.fetchall()
                
            cursor.close()
            return ventas
        except Exception as ex:
            raise Exception(ex)
        
    def detalle_consulta_venta(self,idCarrito):
        try:
            query='SELECT * FROM vista_detalle_carrito WHERE idCarrito=%s'
            conexion= obtener_conexion(USUARIO_CLIENTE)
            productos=[]
            
            with conexion.cursor() as cursor:
                cursor.execute(query, (idCarrito,))
                productos = cursor.fetchall()
            
            conexion.commit()
            cursor.close()
            return productos
            
        except Exception as e:
            raise Exception(e) 

