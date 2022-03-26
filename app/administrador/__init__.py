
from flask import Blueprint, render_template, request, flash

administrador = Blueprint('administrador', __name__)

@administrador.route("/consultar-productos", methods=['GET'])
#@roles_required('administrador')
def consultar_productos_get():
    # consulta de productos en BD
    return 0

@administrador.route("/consultar-producto", methods=['GET'])
#@roles_required('administrador')
def consultar_producto_get():
    # producto_id = request.args.get('id')
    # consulta de producto en BD
    return 0

@administrador.route("/editar-producto", methods=['POST'])
#@roles_required('administrador')
def editar_producto_post():
    #producto.nombre = request.form.get('nombre')
    # Update BD
    return 0

@administrador.route("/eliminar-producto", methods=['POST'])
#@roles_required('administrador')
def editar_producto_post():
    # producto.id = request.form.get('id')
    # producto.activo = 0
    # Update BD
    return 0