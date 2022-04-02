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
        if usuario.idRol == 1:
            flash('No cuentas con permisos para consultar este módulo')
            return render_template('login.html')
        g.user = usuario
    else:
        flash('Es necesario inicar sesión para consultar este módulo')
        return render_template('login.html')


@administrativo.route("/consultar-rendimiento", methods=['GET'])
def consultar_ventas_get():
    if g.user.idRol == 2:
        flash('No cuentas con permisos para consultar este módulo')
        return render_template('/login.html')

    query = QueriesFinanzas()
    monthly = query.ganancia_mes_actual()
    yearly = query.ganancia_anual()
    aux_monthes_earnings = query.ganancia_meses_anio()
    aux_top_10 = query.top_10_productos_vendidos()

    monthes_earnings = [0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0]

    top10_labels = "["
    top10_values = []

    print(aux_top_10)

    for i in aux_top_10:
        if i != aux_top_10[len(aux_top_10)-1]:
            top10_labels += "\"" + str(i[1]) + "\","
        else:
            top10_labels += "\"" + str(i[1]) + "\""
        top10_values.append(i[2])
    top10_labels += "]"

    for i in aux_monthes_earnings:
        monthes_earnings[i[0]] = i[1]

    return render_template('adm/index.html', monthly=monthly, yearly=yearly, monthes_earnings=monthes_earnings, top10_labels=top10_labels, top10_values=top10_values, top10=aux_top_10)
