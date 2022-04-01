from flask import Blueprint, g, session, flash, render_template, redirect, request, url_for
from .Queries.productoQuery import Producto
from ..site import UsuarioQueries
from ..config import USUARIO_ADMINISTATIVO

administrativo = Blueprint('administrativo', __name__, url_prefix='/administrativo')


@administrativo.before_request
def before_request_administrativo():
    if 'id' in session:
        model = UsuarioQueries()
        id = session['id']
        usuario = model.consultar_cliente_por_id(id)
        if usuario.idRol == 1 or usuario.idRol == 2:
            flash('No cuentas con permisos para consultar este módulo')
            return render_template('login.html')
        g.user = usuario
    else:
        flash('Es necesario inicar sesión para consultar este módulo')
        return render_template('login.html')


@administrativo.route("/productos")
def productos():
    query = Producto()
    lista_productos = query.consultarListaProductos(USUARIO_ADMINISTATIVO)
    return render_template('adm/administrativo/catalogo-productos.html', productos=lista_productos)


@administrativo.route("/productos/<product_id>", methods=['GET'])
def detalle_producto(product_id):
    query = Producto()
    producto = query.consultarProducto(USUARIO_ADMINISTATIVO, product_id)
    return render_template('adm/administrativo/consulta-producto.html', producto=producto)


@administrativo.route("/detalle_producto/agregar", methods=['POST'])
def agregar_producto():
    name = request.form.get('nombre')
    desc = request.form.get('descripcion')
    talla = request.form.get('talla')
    image_url = request.form.get('image_url')
    query = Producto()
    resp = query.agregarProducto(name, desc, talla, image_url, USUARIO_ADMINISTATIVO)
    flash(resp)
    return redirect(url_for('administrativo.productos'))


@administrativo.route("/detalle_producto/modificar", methods=['POST'])
def modificar_producto():
    product_id = int(request.form.get('id'))
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    talla = request.form.get('talla')
    image_url = request.form.get('image_url')
    cant_min = request.form.get('cant_min')
    cant_max = request.form.get('cant_max')
    query = Producto()
    query.actualizarProducto(product_id, nombre, descripcion, talla, image_url, cant_min, cant_max,
                             USUARIO_ADMINISTATIVO)
    return redirect(url_for('administrativo.detalle_producto', product_id=product_id))


@administrativo.route("/detalle_producto/eliminar", methods=['POST'])
def eliminar_producto():
    product_id = int(request.form.get('id'))
    status = int(request.form.get('status'))
    query = Producto()
    query.estatus_producto(product_id, status, USUARIO_ADMINISTATIVO)
    return redirect(url_for('administrativo.detalle_producto', product_id=product_id))


@administrativo.route("/consultar-ventas", methods=['GET'])
def consultar_ventas_get():
    return render_template('adm/index.html')


@administrativo.route("/consultar-rendimiento", methods=['GET'])
def consultar_rendimiento_get():
    # calculo de rendimiento
    return
