from flask import Blueprint, render_template, request
from ..config import USUARIO_CLIENTE as USER_TYPE
from .Queries.CarritoProductos import QueriesCarrito as Query


cliente_carrito_name = "CLIENTE_CARRITO"
cliente_carrito_blueprint = Blueprint(cliente_carrito_name, __name__)


@cliente_carrito_blueprint.route("/cliente/carrito-productos/", methods=['GET'])
def carrito_productos():
    
    cliente = 0

    query = Query()
    
    try:
        carrito_usuario = query.carrito_usuario(USER_TYPE, id)

        print(carrito_usuario)
        return render_template('/cliente/carrito.html', carrito=carrito_productos)
    except Exception as e:
        raise e
