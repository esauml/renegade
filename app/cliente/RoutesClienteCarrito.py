from flask import Blueprint, g, render_template, request
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
        return render_template('/cliente/micarrito.html', carrito=carrito_productos)
    except Exception as e:
        raise e
