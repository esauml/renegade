from flask import Blueprint, render_template, request
from ..config import USUARIO_CLIENTE as USER_TYPE
from ..productos.ProductosQueries import Producto as Query


cliente_carrito_name = "CLIENTE_CARRITO"
cliente_carrito_blueprint = Blueprint(cliente_carrito_name, __name__)
