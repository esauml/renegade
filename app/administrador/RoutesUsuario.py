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
    return render_template('adm/index.html')

@usuario.route("/usuario/<id_usuario>", methods=['GET'])
def detalle_usuario(id_usuario):
    return render_template('adm/index.html')

@usuario.route("/usuarios/agregar", methods=['POST'])
def agregar_usuarios():
    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos')
    email = request.form.get('email')
    password = request.form.get('password')

    model = UsuarioQueries()
    usuario_email = model.consultar_por_email(email)

    if usuario_email:
        flash('El correo electrónico ya fue registrado.')
        return redirect(url_for('auth.signup_get'))

    model.registro_usuario(USUARIO_ADMIN, nombre, apellidos, email, password)
    flash('Se registró correctamente al usario.')
    return redirect(url_for('auth.login_get'))

@usuario.route("/usuarios/modificar/<id_usuario>", methods=['GET'])
def modificar_usuario(id_usuario):
    return render_template('adm/index.html')


@usuario.route("/usuario/estatus", methods=['GET'])
def consultar_rendimiento_get():
    # calculo de rendimiento
    return

