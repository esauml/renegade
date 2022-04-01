
from multiprocessing import context
from ..bd import obtener_conexion
import uuid
from datetime import datetime
from ..config import USUARIO_CLIENTE


class Cliente():

    def consultarCliente(self, id):
        try:
            query = 'SELECT * FROM usuario WHERE id={}'.format(1)
            conexion = obtener_conexion(USUARIO_CLIENTE)
            usuario = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                usuario = cursor.fetchall()

            cursor.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)

    def actualizarUsuario(self, nombre, apellidos, email, id):
        try:
            query = 'UPDATE usuario SET nombres = %s, apellidos = %s, correo = %s WHERE id = %s;'
            conexion = obtener_conexion(USUARIO_CLIENTE)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, apellidos, email,  id))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def eliminar_producto(self, id):
        try:
            query = 'UPDATE usuario SET activo = 0 WHERE id = %s'
            conexion = obtener_conexion(USUARIO_CLIENTE)

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def generar_venta(self, id_cliente):
        try:
            self.registrar_venta(id_cliente)
            self.desactivar_carrito_por_cliente(id_cliente)
            self.activar_carrito_por_cliente(id_cliente)
        except Exception as ex:
            raise Exception(ex)

    def registrar_venta(self, id_cliente):
        try:
            folio = str(uuid.uuid4())
            fecha = datetime.today().strftime('%Y-%m-%d')
            carrito = self.obtener_carrito_activo_cliente(id_cliente)
            total = self.calcular_total_carrito_compra(carrito[0])
            query = 'INSERT INTO venta(folio, total, fecha, idCarrito) VALUES (%s, %s, %s, %s);'
            conexion = obtener_conexion(USUARIO_CLIENTE)

            with conexion.cursor() as cursor:
                cursor.execute(query, (folio, total, fecha, carrito[0]))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def obtener_carrito_activo_cliente(self, id_cliente):
        try:
            query = 'SELECT id, status, idUsuario FROM carrito WHERE idUsuario = %s AND status = 1;'
            conexion = obtener_conexion(USUARIO_CLIENTE)
            carrito = []

            with conexion.cursor() as cursor:
                cursor.execute(query, (id_cliente))
                carrito = cursor.fetchone()
                cursor.close()

            if carrito:
                return carrito

            raise Exception(
                "No existe un carrito de compras activo para el cliente.")
        except Exception as ex:
            raise Exception(ex)

    def desactivar_carrito_por_cliente(self, id_cliente):
        try:
            carrito = self.obtener_carrito_activo_cliente(id_cliente)
            query = 'UPDATE carrito SET status = 0 WHERE id = %s;'
            conexion = obtener_conexion(USUARIO_CLIENTE)

            with conexion.cursor() as cursor:
                cursor.execute(query, (carrito[0]))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def activar_carrito_por_cliente(self, id_cliente):
        try:
            query = 'INSERT INTO carrito(status, idUsuario) VALUES (1,%s);'
            conexion = obtener_conexion(USUARIO_CLIENTE)

            with conexion.cursor() as cursor:
                cursor.execute(query, (id_cliente))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def calcular_total_carrito_compra(self, carrito_id):
        try:
            query = 'SELECT sum(suma) FROM (SELECT SUM(cantidad * precio) AS suma FROM carrito  \
                    INNER JOIN productocarrito p on carrito.id = p.idCarrito WHERE idCarrito = %s  \
                    GROUP BY idProducto) AS total;'

            conexion = obtener_conexion(USUARIO_CLIENTE)
            total = []

            with conexion.cursor() as cursor:
                cursor.execute(query, (carrito_id))
                total = cursor.fetchone()
                cursor.close()

            return total
        except Exception as ex:
            raise Exception(ex)

    def calcular_cantidad_disponible_por_producto(self, producto_id):
        # TODO Calculo de materia prima por producto
        return 0
    
    def consulta_mis_ventas(self,tipo_usuario,idCliente):
        try:
            query='SELECT * FROM vista_carritos_usuario WHERE idUsuario={} AND status=0'.format(idCliente)
            conexion= obtener_conexion(tipo_usuario)
            carritos=[]
            
            with conexion.cursor() as cursor:
                cursor.execute(query)
                carritos = cursor.fetchall()
            
            conexion.commit()
            cursor.close()
            return carritos
            
        except Exception as e:
            raise Exception(e)
        
    def detalle_consulta_mis_ventas(self,tipo_usuario,idCarrito):
        try:
            query='SELECT * FROM vista_detalle_carrito WHERE idCarrito={}'.format(idCarrito)
            conexion= obtener_conexion(tipo_usuario)
            productos=[]
            
            with conexion.cursor() as cursor:
                cursor.execute(query)
                productos = cursor.fetchall()
            
            conexion.commit()
            cursor.close()
            return productos
            
        except Exception as e:
            raise Exception(e)
