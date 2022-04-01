from flask import Blueprint, g, redirect, render_template, request, url_for
from ..config import USUARIO_CLIENTE as USER_TYPE
from .Queries.CarritoProductos import QueriesCarrito as Query


cliente_carrito_name = "CLIENTE_CARRITO"
cliente_carrito_blueprint = Blueprint(cliente_carrito_name, __name__)


@cliente_carrito_blueprint.route("/cliente/carrito-productos/", methods=['GET'])
def carrito_productos():

    cliente = g.user.id

    query = Query()

    try:
        carrito_usuario = query.carrito_usuario(USER_TYPE, cliente)

        print(carrito_usuario)
        return render_template('/cliente/micarrito.html', carrito=carrito_usuario)
    except Exception as e:
        raise e

@cliente_carrito_blueprint.route("/cliente/eliminar-producto-carrito", methods=['GET'])
def carrito_productos():

    carrito = request.form.get('id_carrito')
    producto = request.form.get('id_producto')

    query = Query()

    try:
        query.eliminar_producto_de_carrito(USER_TYPE, carrito, producto)
        
        return redirect(url_for('cliente.CLIENTE_CARRITO.carrito_productos'))
    except Exception as e:
        raise e

