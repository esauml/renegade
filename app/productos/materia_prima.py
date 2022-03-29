from ..bd import obtener_conexion


class MateriaPrima():

    def consultar_materias_primas(self, tipo_usuario):
        try:
            query = 'SELECT id, nombre, descripcion, costo, stock FROM materiaprima;'
            conexion = obtener_conexion(tipo_usuario)
            materiasprimas = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                materiasprimas = cursor.fetchall()

            cursor.close()
            return materiasprimas
        except Exception as ex:
            raise Exception(ex)

