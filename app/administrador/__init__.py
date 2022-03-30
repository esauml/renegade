
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, g
from ..productos.ProductosQueries import Producto as Query
from ..config import USUARIO_ADMIN
from ..cliente.clienteQueries import ClienteQueries
from ..site import UsuarioQueries, Rol


administrador = Blueprint('administrador', __name__)


@administrador.before_request
def before_request_cliente():
    if 'id' in session:
        usuario_queries = UsuarioQueries()
        rol_obj = Rol()
        id = session['id']
        usuario = usuario_queries.consultar_cliente_por_id(id)
        roles = rol_obj.obtener_roles_por_usuario_id(id)
        g.user = usuario
        g.rol = roles[0]
        if g.rol == 'cliente' or g.rol == 'administrativo':
            flash('El perfil no cuenta con permisos para consultar esta página.')
            return render_template('login.html')
    else:
        flash('Es necesario inciar sesión previamente.')
        return render_template('login.html')

# HTML Render Entry-Points


@administrador.route("/productos", methods=['GET'])
# @roles_required('administrador')
def consultar_productos_get():
    queries = Query()
    try:
        productos = queries.consultar_productos(USUARIO_ADMIN)
        return render_template('adm/administrador/productos.html', productos=productos)
    except Exception as e:
        # TODO What to do when couldn't handle DB operation
        print("Exception: ")
        raise e
        return render_template('layout.html')


@administrador.route("/detalle-producto/<id>", methods=['GET'])
# @roles_required('administrador')
def consultar_producto_get(id):
    # inputs
    producto_id = id
    # init query handler
    queries = Query()
    # consulta
    try:
        producto_por_id = queries.consultar_producto_por_id(
            USUARIO_ADMIN, producto_id)
        print(producto_por_id)
        return render_template('adm/administrador/detalle-producto.html', producto=producto_por_id)
    except Exception as e:
        raise e


@administrador.route("/editar-producto", methods=['POST'])
# @roles_required('administrador')
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
# @roles_required('administrador')
def eliminar_producto_post():
    id = request.form.get('id')
    queries = Query()
    queries.eliminar_producto(USUARIO_ADMIN, id)
    return redirect(url_for('administrador.consultar_productos_get'))
