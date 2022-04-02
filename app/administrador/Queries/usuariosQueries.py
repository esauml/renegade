from werkzeug.security import generate_password_hash

from ...bd import obtener_conexion



class Usuario():

    def consultar_roles(self, tipo_usuario):
        try:
            query = 'SELECT id, name FROM rol WHERE id <> 1;'
            conexion = obtener_conexion(tipo_usuario)
            roles = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                roles = cursor.fetchall()

            cursor.close()
            return roles
        except Exception as ex:
            raise Exception(ex)

    def consultar_usuarios(self, tipo_usuario):
        try:
            query = 'SELECT u.id,nombres,apellidos,correo,active,idRol, r.name FROM usuario u JOIN rol r on r.id = u.idRol WHERE idRol <> 1;'
            conexion = obtener_conexion(tipo_usuario)
            usuarios = []

            with conexion.cursor() as cursor:
                cursor.execute(query)
                usuarios = cursor.fetchall()

            cursor.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)

    def consultar_por_email(self, email, tipo_usuario):
        try:
            query = "SELECT id, nombres, apellidos, correo, password, active, idRol FROM Usuario WHERE correo = %s"
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (email,))
                consulta = cursor.fetchone()
                cursor.close()

            if consulta != None:
                from ...site.Usuario import Usuario
                return Usuario(consulta[0], consulta[1], consulta[2], consulta[3], consulta[4], consulta[5], consulta[6])

            return None
        except Exception as ex:
            raise Exception(ex)

    def consultar_usuario(self, id_usuario, tipo_usuario):
        try:
            query = 'SELECT id,nombres,apellidos,correo,active,idRol FROM usuario WHERE id = %s;'
            conexion = obtener_conexion(tipo_usuario)
            usuarios = None

            with conexion.cursor() as cursor:
                cursor.execute(query, (id_usuario,))
                usuarios = cursor.fetchone()

            cursor.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)

    def agregar_usuario(self, nombre, apellidos, email, password, rol_id, tipo_usuario):
        try:
            query = 'INSERT INTO Usuario(nombres, apellidos, correo, password, active, idRol) VALUES (%s, %s, %s, %s, 1, %s)'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, apellidos, email,
                               generate_password_hash(password, method='sha256'), rol_id))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def modificar_usuario_w_pd(self, id_usuario, nombre, apellidos, email, password, rol_id, tipo_usuario):
        try:
            query = 'UPDATE Usuario SET nombres = %s, apellidos = %s, correo = %s, password = %s, idRol = %s WHERE id = %s'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, apellidos, email,
                               generate_password_hash(password, method='sha256'), rol_id, id_usuario))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def modificar_usuario(self, id_usuario, nombre, apellidos, email, rol_id, tipo_usuario):
        try:
            query = 'UPDATE Usuario SET nombres = %s, apellidos = %s, correo = %s, idRol = %s WHERE id = %s'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre, apellidos, email, rol_id, id_usuario))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    def estatus_usuario(self, id_usuario, activo, tipo_usuario):
        try:
            query = 'UPDATE Usuario SET active = %s WHERE id = %s'
            conexion = obtener_conexion(tipo_usuario)

            with conexion.cursor() as cursor:
                cursor.execute(query, (activo, id_usuario))

            conexion.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)
