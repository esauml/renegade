from flask import Blueprint, g, session, flash, render_template, redirect, request, url_for
from .Queries.productoQuery import Producto
from ..site import UsuarioQueries
from ..config import USUARIO_ADMINISTATIVO
from .RoutesAdminProducto import producto

administrativo = Blueprint('administrativo', __name__)
administrativo.register_blueprint(producto)

@administrativo.before_request
def before_request_administrativo():
    if 'id' in session:
        model = UsuarioQueries()
        id = session['id']
        usuario = model.consultar_cliente_por_id(id)
        print(id)
        if usuario.idRol == 1 or usuario.idRol == 2:
            flash('No cuentas con permisos para consultar este módulo')
            return render_template('login.html')
        g.user = usuario
    else:
        flash('Es necesario inicar sesión para consultar este módulo')
        return render_template('login.html')

@administrativo.route("/consultar-ventas", methods=['GET'])
def consultar_ventas_get():
    return render_template('adm/index.html')


@administrativo.route("/consultar-rendimiento", methods=['GET'])
def consultar_rendimiento_get():
    # calculo de rendimiento
    return
