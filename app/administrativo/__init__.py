from flask import Blueprint, g, session, flash, render_template, redirect, request, url_for
from .Queries.productoQuery import Producto
from .Queries.FinanzasQuery import QueriesFinanzas
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
        if usuario.idRol == 1:
            flash('No cuentas con permisos para consultar este módulo')
            return render_template('login.html')
        g.user = usuario
    else:
        flash('Es necesario inicar sesión para consultar este módulo')
        return render_template('login.html')

@administrativo.route("/consultar-ventas", methods=['GET'])
def consultar_ventas_get():
    query = QueriesFinanzas()
    
    monthly = query.ganancia_mes_actual()
    yearly = query.ganancia_anual()
    monthes_earnings = query.ganancia_meses_anio()
    top10 = query.top_10_productos_vendidos()
    
    return render_template('adm/index.html', monthly = monthly, yearly = yearly, monthes_earnings = monthes_earnings, top10 = top10)


@administrativo.route("/consultar-rendimiento", methods=['GET'])
def consultar_rendimiento_get():
    # calculo de rendimiento
    return
