
from flask import Blueprint, g, session, flash, render_template
from ..cliente.clienteQueries import Cliente
from ..site import UsuarioQueries

administrativo = Blueprint('administrativo', __name__)


@administrativo.before_request
def before_request_administrativo():
    if 'id' in session:
        model = UsuarioQueries()
        id = session['id']
        usuario = model.consultar_cliente_por_id(id)
        g.user = usuario.before_request


@administrativo.route("/consultar-ventas", methods=['GET'])
def consultar_ventas_get():
    return 0


@administrativo.route("/consultar-rendimiento", methods=['GET'])
def consultar_rendimiento_get():
    # calculo de rendimiento
    return 0
