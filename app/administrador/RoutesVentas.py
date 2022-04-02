from flask import Blueprint, g, session, flash, render_template, redirect, request, url_for
from .Queries.ventaQueries import Venta
from ..site import UsuarioQueries
from ..config import USUARIO_ADMIN

ventas = Blueprint('ventas', __name__, url_prefix='/admin')

@ventas.before_request
def before_request_administrativo():
    if 'id' in session:
        model = UsuarioQueries()
        id = session['id']
        usuario = model.consultar_cliente_por_id(id)
        print(id)
        if usuario.idRol == 1:
            flash('No cuentas con permisos para consultar este módulo')
            return render_template('login.html')
        g.user = usuario
    else:
        flash('Es necesario inicar sesión para consultar este módulo')
        return render_template('login.html')

@ventas.route("/catalogo_ventas", methods=['GET'])
def getVentas():
    query = Venta()
    ventas = query.consultar_ventas()
    return render_template('adm/administrador/catalogo-ventas.html', ventas=ventas)

@ventas.route("/detalle-venta/<id>", methods=['GET'])
def getDetalleVentas(id):
    query = Venta()
    ventas = query.detalle_consulta_venta(id)
    return render_template('adm/administrador/detalle-ventas.html', ventas=ventas)