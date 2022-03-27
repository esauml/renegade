from ..bd import obtener_conexion
from flask_security import RoleMixin

class Rol(RoleMixin):

    def agregar_rol_cliente_por_id(self, tipo_usuario, id):
        query = 'INSERT INTO usuario_rol(usuario_id, rol_id) VALUES (%s, 3);'
        conexion = obtener_conexion(tipo_usuario)

        with conexion.cursor() as cursor:
            cursor.execute(query, (id))

        conexion.commit()
        cursor.close()