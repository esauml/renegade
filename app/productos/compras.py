from ..bd import obtener_conexion
import uuid
class Compras():
    
    def consultar_compras(self, tipo_usuario):
        try:
            query = 'SELECT * FROM vista_compras;'
            conexion = obtener_conexion(tipo_usuario)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)
        
    def consultar_compra_id(self, tipo_usuario, id):
        try:
            query = 'SELECT * FROM vista_compras WHERE id=%s;'
            conexion = obtener_conexion(tipo_usuario)
            materia = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                materia = cursor.fetchone()

            cursor.close()
            return materia
        except Exception as ex:
            raise Exception(ex)
    
    def consultar_materias_compra(self, tipo_usuario, id):
        try:
            query = 'SELECT * FROM vista_lista_materiasCompra WHERE id=%s;'
            conexion = obtener_conexion(tipo_usuario)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query,(id,))
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)
    
    def consultar_materia_select(self, tipo_usuario):
        try:
            query = 'SELECT * FROM MateriaPrima;'
            conexion = obtener_conexion(tipo_usuario)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)
    
    def consultar_proveedor_select(self, tipo_usuario):
        try:
            query = 'SELECT * FROM Proveedor;'
            conexion = obtener_conexion(tipo_usuario)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)
    def consultar_materia_id(self, tipo_usuario, id):
        try:
            query = 'SELECT m.*, com.costo FROM MateriaPrima  as m inner join \
                CompraStockMateria as com on m.id=com.idMateriaPrima\
                WHERE id=%s;'
            conexion = obtener_conexion(tipo_usuario)
            materia = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                materia = cursor.fetchone()

            cursor.close()
            return materia
        except Exception as ex:
            raise Exception(ex)
    
    
    def asignarFolio(self, tipo_usuario):
        folio = str(uuid.uuid4())
        return folio;
        
    