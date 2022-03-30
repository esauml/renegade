from ..bd import obtener_conexion
from ..config import USUARIO_CLIENTE
from ..site.UsuarioQueries import UsuarioQueries


class ClienteQueries():

    def consultar_perfil(self, id):
        usuario_queries = UsuarioQueries()
        usuario = usuario_queries.consultar_cliente_por_id(id)
        if usuario:
            usuario.password = None
            return usuario

        return None
