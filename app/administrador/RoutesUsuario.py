from flask import Blueprint, g, session, flash, render_template, redirect, request, url_for
from .Queries.usuariosQueries import Usuario
from ..site import UsuarioQueries
from ..config import USUARIO_ADMIN

usuario = Blueprint('usuario', __name__, url_prefix='/admin')

@usuario.before_request
def before_request_administrativo():
    if 'id' in session:
        model = UsuarioQueries()
        id = session['id']
        usuario = model.consultar_cliente_por_id(id)
        print(id)
        if usuario.idRol == 1 or usuario.idRol == 3:
            flash('No cuentas con permisos para consultar este módulo')
            return render_template('login.html')
        g.user = usuario
    else:
        flash('Es necesario inicar sesión para consultar este módulo')
        return render_template('login.html')

@usuario.route("/usuarios", methods=['GET'])
def usuarios():
    query = Usuario()
    usuarios = query.consultar_usuarios(USUARIO_ADMIN)
    roles = query.consultar_roles(USUARIO_ADMIN)
    return render_template('adm/administrador/catalogo-usuarios.html', usuarios=usuarios, roles=roles)

@usuario.route("/usuario/<id_usuario>", methods=['GET'])
def detalle_usuario(id_usuario):
    query = Usuario()
    u = query.consultar_usuario(id_usuario, USUARIO_ADMIN)
    roles = query.consultar_roles(USUARIO_ADMIN)
    return render_template('adm/administrador/detalle-usuario.html', usuario=u, roles=roles)

@usuario.route("/usuarios/agregar", methods=['POST'])
def agregar_usuarios():
    query = Usuario()

    nombre = request.form.get('nombres')
    apellidos = request.form.get('apellidos')
    email = request.form.get('correo')
    password = request.form.get('password')
    rol_id = request.form.get('rol_id')

    usuario_email = query.consultar_por_email(email, USUARIO_ADMIN)

    if usuario_email:
        flash('El correo electrónico ya fue registrado.')
        return redirect(url_for('administrador.usuario.usuarios'))

    query.agregar_usuario(nombre, apellidos, email, password, rol_id, USUARIO_ADMIN)
    flash('Se registró correctamente al usario.')
    return redirect(url_for('administrador.usuario.usuarios'))

@usuario.route("/usuarios/modificar/<id_usuario>", methods=['POST'])
def modificar_usuario(id_usuario):
    query = Usuario()

    nombre = request.form.get('nombres')
    apellidos = request.form.get('apellidos')
    email = request.form.get('correo')
    password = request.form.get('password')
    rol_id = request.form.get('rol_id')
    usuario_email = query.consultar_por_email(email, USUARIO_ADMIN)

    if usuario_email:
        flash('El correo electrónico ya fue registrado.')
        return redirect(url_for('administrador.usuario.detalle_usuario', id_usuario=id_usuario))

    if password == '':
        query.modificar_usuario(id_usuario, nombre, apellidos, email, rol_id, USUARIO_ADMIN)
    else:
        query.modificar_usuario_w_pd(id_usuario, nombre, apellidos, email, password, rol_id, USUARIO_ADMIN)

    flash('Se modificó correctamente al usario.')
    return redirect(url_for('administrador.usuario.detalle_usuario', id_usuario=id_usuario))


@usuario.route("/usuario/<id_usuario>/estatus", methods=['POST'])
def estatus_usuario(id_usuario):
    status = request.form.get('status')
    query = Usuario()
    query.estatus_usuario(id_usuario, status, USUARIO_ADMIN)
    return redirect(url_for('administrador.usuario.usuarios'))

