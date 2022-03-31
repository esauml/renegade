
from flask import Blueprint, g, session, flash, render_template
from ..cliente.clienteQueries import Cliente
from ..site import UsuarioQueries

administrativo = Blueprint('administrativo', __name__)


@administrativo.route("/consultar-ventas", methods=['GET'])
def consultar_ventas_get():
    return 0

@administrativo.route("/consultar-rendimiento", methods=['GET'])
def consultar_rendimiento_get():
    # calculo de rendimiento
    return 0