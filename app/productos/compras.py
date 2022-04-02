from ..bd import obtener_conexion
from ..config import USUARIO_ADMIN
import uuid


class Compras():
<<<<<<< HEAD
    
    def consultar_compras(self):
        try:
            query = 'SELECT * FROM vista_compras;'
            conexion = obtener_conexion(USUARIO_ADMIN)
=======

    def consultar_compras(self, tipo_usuario):
        try:
            query = 'SELECT * FROM vista_compras_surtidas;'
            conexion = obtener_conexion(tipo_usuario)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)

    def consultar_compras_nosurtidas(self, tipo_usuario):
        try:
            query = 'SELECT * FROM vista_compras_nosurtidas;'
            conexion = obtener_conexion(tipo_usuario)
>>>>>>> oscar
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)
<<<<<<< HEAD
        
    def consultar_compra_id(self, id):
=======

    def consultar_compra_id(self, tipo_usuario, id):
>>>>>>> oscar
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
<<<<<<< HEAD
    
    def consultar_materias_compra(self, id):
=======

    def consultar_compranosurtida_id(self, tipo_usuario, id):
        try:
            query = 'SELECT * FROM vista_compras_nosurtidas WHERE id=%s;'
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
>>>>>>> oscar
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
<<<<<<< HEAD
    
    def consultar_materia_select(self):
=======

    def consultar_materias_compranosurtidas(self, tipo_usuario, id):
        try:
            query = 'SELECT * FROM vista_materias_nosurtidas WHERE id=%s;'
            conexion = obtener_conexion(tipo_usuario)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)

    def consultar_materia_select(self, tipo_usuario):
>>>>>>> oscar
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
<<<<<<< HEAD
    
    def consultar_proveedor_select(self):
=======

    def consultar_proveedor_select(self, tipo_usuario):
>>>>>>> oscar
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

<<<<<<< HEAD
    def consultar_materia_id(self, id):
        try:
            query = 'SELECT m.*, com.costo FROM MateriaPrima  as m inner join \
                CompraStockMateria as com on m.id=com.idMateriaPrima\
                WHERE id=%s;'
            conexion = obtener_conexion(USUARIO_ADMIN)
=======
    def consultar_materia_id(self, tipo_usuario, id):
        try:
            query = 'SELECT * FROM MateriaPrima WHERE id=%s;'
            conexion = obtener_conexion(tipo_usuario)
>>>>>>> oscar
            materia = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                materia = cursor.fetchone()

            cursor.close()
            return materia
        except Exception as ex:
            raise Exception(ex)
<<<<<<< HEAD
    
    
    def asignarFolio(self):
        folio = str(uuid.uuid4())
        return folio
        
    
    def insertar_compra(self, tipo_usuario,folio, fecha, proveedor, listaMaterias):
        try:            
=======

    def asignarFolio(self, tipo_usuario):
        folio = str(uuid.uuid4())
        return folio

    def insertarCompraStockMateria(tipo_usuario, idOrdenCompra, materia):
        try:
            query = 'INSERT INTO CompraStockMateria (idOrdenCompra, idMateriaPrima, Cantidad, costo) \
                    values (%s,%s,%s,%s);'
            conexion = obtener_conexion(tipo_usuario)

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

    def insertar_compra(self, tipo_usuario, folio, fecha, listaMaterias):
        try:
            query = 'INSERT INTO Compra (folio, fechaCompra) \
                    values (%s,%s);'
            query2 = 'INSERT INTO CompraStockMateria (idOrdenCompra, idMateriaPrima, Cantidad) \
                    values (%s,%s,%s);'
            conexion = obtener_conexion(tipo_usuario)
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

    def insertar_arribo(self, tipo_usuario, folio, fecha, proveedor, listaMaterias):
        try:
>>>>>>> oscar
            query = 'INSERT INTO Compra (folio, idProveedor, fechaCompra) \
                    values (%s,%s,%s);'

            query2 = 'INSERT INTO CompraStockMateria (idOrdenCompra, idMateriaPrima, Cantidad, costo) \
                    values (%s,%s,%s,%s);'

            query3 = 'INSERT INTO StockMateriaPrima (cantidad, idMateriaPrima, idOrdenCompra) \
                    values (%s,%s,%s);'

            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (folio, proveedor, fecha))
            valCompraStockMateria = []
            valStockMateria = []
            idOrdenCompra = conexion.insert_id()

            for materia in listaMaterias:
                print(materia)
                list1 = (idOrdenCompra, int(materia['id']), int(
                    materia['cantidad']), materia['costo'])
                valCompraStockMateria.append(list1)
                
                print(valCompraStockMateria)

                for i in range(int(materia['cantidad'])):

                    list2 = (int(materia['cant']), int(
                        materia['id']), idOrdenCompra)
                    print("aqui estan los val de StockMateria .  . . . . .. . . . ")
                    print("aqui estan los val de StockMateria .  . . . . .. . . . ")
                    print("aqui estan los val de StockMateria .  . . . . .. . . . ")
                    print("aqui estan los val de StockMateria .  . . . . .. . . . ")
                    print("aqui estan los val de StockMateria .  . . . . .. . . . ")
                    valStockMateria.append(list2)
                    print(valStockMateria)

            with conexion.cursor() as cursor2:
                cursor2.executemany(query2, valCompraStockMateria)

            with conexion.cursor() as cursor3:
                cursor3.executemany(query3, valStockMateria)
            conexion.commit()

            cursor.close()

        except Exception as ex:
            raise Exception(ex)
        return
