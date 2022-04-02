from ...bd import obtener_conexion

class Usuario():

    def consultar_usuarios(self, tipo_usuario):
        try:
            query = 'SELECT * FROM usuario WHERE idRol <> 1;'
            conexion = obtener_conexion(tipo_usuario)
            usuarios = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                usuarios = cursor.fetchall()

            cursor.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)
