
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, g
from ..productos.ProductosQueries import Producto as Query
from .proveedoresQueries import ProveedoresQueries as QueryProveedores
from ..config import USUARIO_ADMIN
from ..cliente.clienteQueries import Cliente
from ..site import UsuarioQueries

administrador = Blueprint('administrador', __name__)


@administrador.before_request
def before_request_administrador():
    if 'id' in session:
        model = UsuarioQueries()
        id = session['id']
        usuario = model.consultar_cliente_por_id(id)
        g.user = usuario
    else:
        flash('Es necesario inicar sesión para consultar este módulo')
        return render_template('login.html')


@administrador.route("/productos", methods=['GET'])
def consultar_productos_get():
    queries = Query()
    productos = queries.consultar_productos(USUARIO_ADMIN)
    return render_template('adm/administrador/productos.html', productos=productos)


@administrador.route("/detalle-producto/<id>", methods=['GET'])
def consultar_producto_get(id):
    # inputs
    producto_id = id
    # init query handler
    queries = Query()
    # consulta
    producto_por_id = queries.consultar_producto_por_id(
        USUARIO_ADMIN, producto_id)
    print(producto_por_id)
    return render_template('adm/administrador/detalle-producto.html', producto=producto_por_id)


@administrador.route("/editar-producto", methods=['POST'])
def editar_producto_post():
    # TODO Validar formulario
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio = request.form.get('precio')
    id = request.form.get('id')

    queries = Query()
    queries.actualizar_producto(USUARIO_ADMIN, nombre, descripcion, precio, id)
    return redirect(url_for('administrador.consultar_productos_get'))


@administrador.route("/eliminar-producto", methods=['POST'])
def eliminar_producto_post():
    id = request.form.get('id')
    queries = Query()
    queries.eliminar_producto(USUARIO_ADMIN, id)
    return redirect(url_for('administrador.consultar_productos_get'))


@administrador.route("/consultar-proveedores", methods=['GET'])
def consultar_proveedores():
    queries = QueryProveedores()
    proveedores = queries.consultar_proveedores()
    return render_template('adm/administrador/proveedores.html', proveedores=proveedores)
