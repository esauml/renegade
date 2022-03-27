
from flask import Blueprint

administrativo = Blueprint('administrativo', __name__)

@administrativo.route("/consultar-ventas", methods=['GET'])
#@roles_required('administrativo')
def consultar_ventas_get():
    return 0

@administrativo.route("/consultar-rendimiento", methods=['GET'])
#@roles_required('administrativo')
def consultar_rendimiento_get():
    # calculo de rendimiento
    return 0