from ..bd import obtener_conexion
from ..config import USUARIO_ADMIN

class MateriaPrima():

    def consultar_materias_primas(self):
        try:
            query = 'SELECT * FROM vista_materia_lista;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)

    def consultar_materia_prima_id(self, id):
        try:
            query = 'SELECT * FROM vista_materia_lista WHERE id=%s;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            materia = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                materia = cursor.fetchone()

            cursor.close()
            return materia
        except Exception as ex:
            raise Exception(ex)

    def consultar_listamaterias_prima_id(self, id):
        try:
            query = 'SELECT * FROM vista_materia_lista_id WHERE id=%s;'
            conexion = obtener_conexion(USUARIO_ADMIN)
            materia = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                materia = cursor.fetchall()

            cursor.close()
            return materia
        except Exception as ex:
            raise Exception(ex)
        
    def actualizar_materia(self, nombre, descripcion, id):
        try:
            query = 'UPDATE MateriaPrima SET nombre = %s, descripcion = %s WHERE id = %s;'
            conexion = obtener_conexion(USUARIO_ADMIN)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, descripcion, id))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def guardar_materia(self, nombre, descripcion, cantidad, unidad):
        try:
            query = 'INSERT INTO MateriaPrima (nombre, descripcion, cantidad, unidad) \
                    values (%s,%s,%s,%s);'
            conexion = obtener_conexion(USUARIO_ADMIN)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, descripcion, cantidad, unidad))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)
