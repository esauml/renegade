from flask import Blueprint, redirect, render_template, request, url_for
from ..config import USUARIO_CLIENTE as USER_TYPE
from .Queries.Productos import QueriesProducto as Query
from .Queries.CarritoProductos import QueriesCarrito as QueryCarrito


cliente_productos_name = "CLIENTE_PRODUCTOS"
cliente_productos_blueprint = Blueprint(cliente_productos_name, __name__)


@cliente_productos_blueprint.route('/cliente/listado-productos', methods=["GET"])
def listado_productos():
    queries = Query()
    try:
        productos = queries.consultar_productos(USER_TYPE)
        return render_template('cliente/catalogo-productos.html', productos=productos)
    except Exception as e:
        # TODO What to do when couldn't handle DB operation
        print("Exception: ")
        raise e
        return render_template('layout.html')


# Viene Después de hacer una busqueda <FORM>
@cliente_productos_blueprint.route('/cliente/productos-busqueda', methods=["POST"])
def productos_busqueda():
    criteria = request.form.get('criteria')

    queries = Query()
    try:
        productos = queries.consultar_productos_busqueda(USER_TYPE, criteria)
        return render_template('cliente/catalogo-productos.html', productos=productos)
    except Exception as e:
        print('Exception: ')
        raise e


@cliente_productos_blueprint.route("/cliente/detalle-producto/<id>", methods=['GET'])
def consultar_producto_get(id):
    # inputs
    producto_id = id
    # init query handler
    queries = Query()
    # consulta
    try:
        producto_por_id = queries.consultar_producto_por_id(
            USER_TYPE, producto_id)

        stock = 0  # default for now

        print(producto_por_id)
        return render_template('cliente/detalle-producto.html', producto=producto_por_id)
    except Exception as e:
        raise e


@cliente_productos_blueprint.route("/cliente/max-possible-stock/<id>", methods=['GET'])
def max_possible_stock(id):
    # inputs
    producto_id = id
    # init query handler
    queries = Query()
    # consulta
    try:

        # MAX POSSIBLE STOCK FOR SPECIFIC PRODUCT
        # stock = queries.consultar_calculo_max_stock(USER_TYPE, producto_id)
        stock = 0  # default for now

        print(f'Max Calculated Stock For Producto({id}). Stock: {stock}')
        return {'max_stock': stock}
    except Exception as e:
        raise e


@cliente_productos_blueprint.route("/cliente/agregar-producto-producto", methods=['POST'])
def aregar_producto_carrito():
    # inputs
    cliente = request.form.get('id-cliente')
    producto = request.form.get('id-producto') 
    cantidad = request.form.get('cantidad')


    # init query handler
    queries = QueryCarrito()
    # consulta
    try:
        queries.agregar_producto(
            USER_TYPE, cliente, producto, cantidad)

        return redirect(url_for('CLIENTE_CARRITO.carrito_productos'))
    except Exception as e:
        raise e
