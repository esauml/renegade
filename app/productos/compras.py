from ast import USub
from ..bd import obtener_conexion
from ..config import USUARIO_ADMIN
import uuid


class Compras():

    def consultar_compras(self):
        try:
            query = 'SELECT * FROM vista_compras_surtidas;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)

    def consultar_compras_nosurtidas(self):
        try:
            query = 'SELECT * FROM vista_compras_nosurtidas;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)
        
    def consultar_compra_id(self, id):
        try:
            query = 'SELECT * FROM vista_compras_surtidas WHERE idOrdenCompra=%s;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            materia = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                materia = cursor.fetchone()

            cursor.close()
            return materia
        except Exception as ex:
            raise Exception(ex)
        
    def consultar_materias_orden(self,  id):
        try:
            query = 'SELECT m.*, com.idOrdenCompra \
                    FROM MateriaPrima as m INNER JOIN compraStockMateria as com on m.id=com.idMateriaPrima \
                    WHERE com.idOrdenCompra=%s ORDER BY com.idOrdenCompra ;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            materia = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (int(id),))
                materia = cursor.fetchall()

            cursor.close()
            return materia
        except Exception as ex:
            raise Exception(ex)

    def consultar_compranosurtida_id(self,  id):
        try:
            query = 'SELECT * FROM vista_compras_nosurtidas WHERE id=%s;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            materia = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                materia = cursor.fetchone()

            cursor.close()
            return materia
        except Exception as ex:
            raise Exception(ex)

    def consultar_materias_compra(self, id):
        try:
            query = 'SELECT * FROM vista_lista_materias_compradas WHERE idOrdenCompra=%s;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)
    
    def consultar_materias_compranosurtidas(self, id):
        try:
            query = 'SELECT * FROM vista_materias_nosurtidas WHERE id=%s;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query,(id,))
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)
    
    def consultar_materia_select(self):
        try:
            query = 'SELECT * FROM MateriaPrima;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)
    
    def consultar_compra_select(self):
        try:
            query = 'SELECT * FROM Compra;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            compras = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                compras = cursor.fetchall()

            cursor.close()
            return compras
        except Exception as ex:
            raise Exception(ex)
    
    def consultar_proveedor_select(self):
        try:
            query = 'SELECT * FROM Proveedor;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)

    def consultar_materia_id(self, id):
        try:
            query = 'SELECT * FROM MateriaPrima WHERE id=%s;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            materia = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                materia = cursor.fetchone()

            cursor.close()
            return materia
        except Exception as ex:
            raise Exception(ex)

    def asignarFolio(self):
        folio = str(uuid.uuid4())
        return folio

    def insertarCompraStockMateria( idOrdenCompra, materia):
        try:
            query = 'INSERT INTO CompraStockMateria (idOrdenCompra, idMateriaPrima, Cantidad, costo) \
                    values (%s,%s,%s,%s);'
            conexion = obtener_conexion(USUARIO_ADMIN)

            with conexion.cursor() as cursor:
                cursor.execute(
                    query, (idOrdenCompra, materia['id'], materia['cantidad'], materia['costo']))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)
        return

    def insertarStockMateria(tipo_usuario, idOrdenCompra, idMateriaPrima, cantidad):
        try:
            query = 'INSERT INTO StockMateria (cantidad, idMateriaPrima, idOrdenCompra) \
                    values (%s,%s,%s);'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(
                    query, (idOrdenCompra, idMateriaPrima, cantidad))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)
        return

    def insertar_compra(self, folio, fecha, listaMaterias):
        try:
            query = 'INSERT INTO Compra (folio, fechaCompra) \
                    values (%s,%s);'
            query2 = 'INSERT INTO CompraStockMateria (idOrdenCompra, idMateriaPrima, Cantidad) \
                    values (%s,%s,%s);'
            conexion = obtener_conexion(USUARIO_ADMIN)
            with conexion.cursor() as cursor:
                cursor.execute(query, (folio, fecha))
            valCompraStockMateria = []
            idOrdenCompra = conexion.insert_id()
            for materia in listaMaterias:
                print(materia)
                
                list1 = (idOrdenCompra, int(materia['id']), int(materia['cantidad']))
                valCompraStockMateria.append(list1)
                
            with conexion.cursor() as cursor2:
                cursor2.executemany(query2, valCompraStockMateria)
            conexion.commit()

            cursor.close()
            cursor2.close()
        except Exception as ex:
            raise Exception(ex)

        return

    def actualizarEstatusCompra(self, id):
        try:
            query = 'UPDATE Compra SET surtida = 1 WHERE id = %s;'
            conexion = obtener_conexion(USUARIO_ADMIN)

            with conexion.cursor() as cursor:
                cursor.execute(query, (id))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)
        
    
    def insertar_arribo(self, folio, fecha, idOrdenCompra, proveedor, listaMaterias):
        try:
            query = 'INSERT INTO arriboInsumos (idProveedor, fechaArribo, folioArribo, idOrdenCompra) \
                    values (%s,%s,%s, %s);'

            query2 = 'INSERT INTO arriboMateria (idArriboInsumos, idMateriaPrima, Cantidad, costo) \
                    values (%s,%s,%s,%s);'

            query3 = 'INSERT INTO StockMateriaPrima (cantidad, idMateriaPrima, idArriboInsumos) \
                    values (%s,%s,%s);'

            conexion = obtener_conexion(USUARIO_ADMIN)

            with conexion.cursor() as cursor:
                cursor.execute(query, (proveedor, fecha, folio, idOrdenCompra))
            valArriboMateria = []
            valStockMateria = []
            idArriboInsumos = conexion.insert_id()

            for materia in listaMaterias:
                print(materia)
                list1 = (idArriboInsumos, int(materia['id']), int(materia['cantidad']), materia['costo'])
                valArriboMateria.append(list1)                
                print(valArriboMateria)

                for i in range(int(materia['cantidad'])):
                    list2 = (int(materia['cant']), int(materia['id']), idArriboInsumos)                    
                    valStockMateria.append(list2)

            with conexion.cursor() as cursor2:
                cursor2.executemany(query2, valArriboMateria)

            with conexion.cursor() as cursor3:
                cursor3.executemany(query3, valStockMateria)
            conexion.commit()

            cursor.close()

        except Exception as ex:
            raise Exception(ex)
        return
