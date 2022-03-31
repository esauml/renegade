from flask import Blueprint, g, session, flash, render_template
from .Queries.productoQuery import Producto
from ..site import UsuarioQueries
from ..config import USUARIO_ADMINISTATIVO

administrativo = Blueprint('administrativo', __name__, url_prefix='/administrativo')


@administrativo.before_request
def before_request_administrativo():
    if 'id' in session:
        model = UsuarioQueries()
        id = session['id']
        usuario = model.consultar_cliente_por_id(id)
        g.user = usuario


@administrativo.route("/productos", methods=['GET'])
def productos():
    query = Producto()
    lista_productos = query.consultarListaProductos(USUARIO_ADMINISTATIVO)
    return render_template('adm/administrativo/catalogo-productos.html', productos=lista_productos)


@administrativo.route("/detalle_producto/<product_id>", methods=['GET'])
def detalle_producto(product_id):
    return render_template('adm/administrativo/consulta-producto.html')


@administrativo.route("/consultar-ventas", methods=['GET'])
def consultar_ventas_get():
    return render_template('adm/index.html')


@administrativo.route("/consultar-rendimiento", methods=['GET'])
def consultar_rendimiento_get():
    # calculo de rendimiento
    return
