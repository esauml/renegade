from flask import Blueprint, render_template, request
from ..config import USUARIO_CLIENTE as USER_TYPE
from ..productos.ProductosQueries import Producto as Query


cliente_productos_name = "CLIENTE_PRODUCTOS"
cliente_productos_blueprint = Blueprint(cliente_productos_name, __name__)


@cliente_productos_blueprint.route('listado-productos', methods=["GET"])
def listado_productos():
    queries = Query()
    try:
        productos = queries.consultar_productos(USER_TYPE)
        return render_template('clientes/productos.html', productos=productos)
    except Exception as e:
        # TODO What to do when couldn't handle DB operation
        print("Exception: ")
        raise e
        return render_template('layout.html')


# Viene Después de hacer una busqueda <FORM>
@cliente_productos_blueprint.route('productos-busqueda', methods=["POST"])
def productos_busqueda():
    criteria = request.form.get('criteria')

    queries = Query()
    try:
        productos = queries.consultar_productos_busqueda(USER_TYPE)
        return render_template('clientes/productos.html', productos=productos)
    except Exception as e:
        print('Exception: ')
        raise e


@cliente_productos_blueprint.route("/detalle-producto/<id>", methods=['GET'])
def consultar_producto_get(id):
    # inputs
    producto_id = id
    # init query handler
    queries = Query()
    # consulta
    try:
        producto_por_id = queries.consultar_producto_por_id(
            USER_TYPE, producto_id)

        # STOCK FOR SPECIFIC
        # stock = queries.consultar_stock_producto(USER_TYPE, producto_id)
        stock = 0  # default for now

        print(producto_por_id)
        return render_template('administrador/detalle-producto.html', producto=producto_por_id, stock=stock)
    except Exception as e:
        raise e


@cliente_productos_blueprint.route("/max-possible-stock/<id>", methods=['GET'])
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
