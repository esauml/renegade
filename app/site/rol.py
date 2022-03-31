from ..bd import obtener_conexion
from flask_security import RoleMixin
from ..config import USUARIO_ADMIN


class Rol(RoleMixin):

    def obtener_roles_por_usuario_id(self, id):
        try:
            query = 'SELECT R.name FROM usuario u \
                 INNER JOIN Rol_Usuario right outer join Rol_Usuario RU on u.id = RU.idUsuario \
                 INNER JOIN Rol R on Rol_Usuario.idRol = R.id \
                 WHERE u.id = %s;'

            conexion = obtener_conexion(USUARIO_ADMIN)
            rol = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id,))
                rol = cursor.fetchone()

            cursor.close()
            # TODO self.calcular_cantidad_disponible_por_producto(producto[0]).
            return rol
        except Exception as ex:
            raise Exception(ex)
