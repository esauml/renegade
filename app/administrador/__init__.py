
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, g

from app.productos import materia_prima

from ..productos.ProductosQueries import Producto as Query
from .proveedoresQueries import ProveedoresQueries as QueryProveedores
from ..config import USUARIO_ADMIN
from ..cliente.clienteQueries import Cliente
from ..site import UsuarioQueries
from .RoutesUsuario import usuario

administrador = Blueprint('administrador', __name__)
administrador.register_blueprint(usuario)


@administrador.before_request
def before_request_administrador():
    if 'id' in session:
        model = UsuarioQueries()
        id = session['id']
        usuario = model.consultar_cliente_por_id(id)
        if usuario.idRol == 1 or usuario.idRol == 3:
            flash('No cuentas con permisos para consultar este módulo')
            return render_template('login.html')
        g.user = usuario
    else:
        flash('Es necesario inicar sesión para consultar este módulo')
        return render_template('login.html')


@administrador.route("/consultar-proveedores", methods=['GET'])
def consultar_proveedores():
    queries = QueryProveedores()
    proveedores = queries.consultar_proveedores()
    return render_template('adm/administrador/proveedores.html', proveedores=proveedores)


@administrador.route("/consultar-proveedor/<id>", methods=['GET'])
def consultar_proveedore_get(id):
    queries = QueryProveedores()
    proveedor = queries.consultar_proveedor_por_id(id)

    if proveedor:
        materia_primas = queries.consultar_materiasprimas_por_proveedor_id(
            proveedor[0])
        return render_template('adm/administrador/detalle-proveedor.html', proveedor=proveedor, materia_primas=materia_primas)

    flash('El proveedor no existe.')
    return redirect(url_for('administrador.consultar_proveedores'))


@administrador.route("/agregar-proveedor", methods=['GET'])
def agregar_proveedor_get():
    return render_template('adm/administrador/agregar-proovedor.html')


@administrador.route("/agregar-proveedor", methods=['POST'])
def agregar_proveedor_post():
    nombre = request.form.get('nombre')
    contacto = request.form.get('contacto')
    telefono = request.form.get('telefono')
    correo = request.form.get('correo')

    queries = QueryProveedores()
    queries.guardar_proveedor(nombre, correo, contacto, telefono)

    flash('Se creó correctamente al proveedor.')
    return redirect(url_for('administrador.consultar_proveedores'))


@administrador.route("/actualizar-proveedor", methods=['POST'])
def actualizar_proveedor_post():
    id = request.form.get('id')
    nombre = request.form.get('nombre')
    contacto = request.form.get('contacto')
    telefono = request.form.get('telefono')
    correo = request.form.get('correo')

    queries = QueryProveedores()
    queries.actualizar_proveedor(nombre, correo, contacto, telefono, id)

    flash('Se actualizó correctamente al proveedor.')
    return redirect(url_for('administrador.consultar_proveedores'))
