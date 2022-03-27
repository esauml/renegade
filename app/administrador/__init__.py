
from flask import Blueprint, render_template, request, redirect, url_for
from ..productos import producto
from ..config import USUARIO_ADMIN


administrador = Blueprint('administrador', __name__)

@administrador.route("/consultar-productos", methods=['GET'])
#@roles_required('administrador')
def consultar_productos_get():
    producto_obj = producto.Producto()
    productos = producto_obj.consultar_productos(USUARIO_ADMIN)
    return render_template('catalogo-productos.html', productos = productos)

@administrador.route("/consultar-producto", methods=['GET'])
#@roles_required('administrador')
def consultar_producto_get():
    producto_id = request.args.get('id')
    producto_obj = producto.Producto()
    producto_por_id = producto_obj.consultar_producto_por_id(USUARIO_ADMIN, producto_id)
    print(producto_por_id)
    return render_template('consulta-producto.html', producto = producto_por_id)

@administrador.route("/editar-producto", methods=['POST'])
#@roles_required('administrador')
def editar_producto_post():
    #TODO Validar formulario
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio = request.form.get('precio')
    id = request.form.get('id')

    producto_obj = producto.Producto()
    producto_obj.actualizar_producto(USUARIO_ADMIN, nombre, descripcion, precio, id)
    return redirect(url_for('administrador.consultar_productos_get'))

@administrador.route("/eliminar-producto", methods=['POST'])
#@roles_required('administrador')
def eliminar_producto_post():
    id = request.form.get('id')
    producto_obj = producto.Producto()
    producto_obj.eliminar_producto(USUARIO_ADMIN, id)
    return redirect(url_for('administrador.consultar_productos_get'))