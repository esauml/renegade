from ..bd import obtener_conexion


class MateriaPrima():

    def consultar_materias_primas(self, tipo_usuario):
        try:
            query = 'SELECT * FROM vista_stock_materia;'
            conexion = obtener_conexion(tipo_usuario)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)

    def consultar_materia_prima_id(self, tipo_usuario, id):
        try:
            query = 'SELECT * FROM vista_stock_materia WHERE id=%s;'
            conexion = obtener_conexion(tipo_usuario)
            materia = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                materia = cursor.fetchone()

            cursor.close()
            return materia
        except Exception as ex:
            raise Exception(ex)
