
from flask import Blueprint, render_template, request, flash, g

cliente = Blueprint('cliente', __name__)

@cliente.route("/carrito-compras", methods=['GET'])
#@roles_required('cliente')
def consultar_ventas_get():
    # current_user()
    # consulta de carrito en BD
    return 0

@cliente.route("/agregar-producto-carrito", methods=['POST'])
#@roles_required('cliente')
def agregar_producto_carrito_post():
    # id producto
    #cantidad
    return 0

@cliente.route("/profile", methods=['GET'])
def profile_get():
    return ""
