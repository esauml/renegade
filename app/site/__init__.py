from flask import Blueprint, render_template, request, flash, redirect, url_for, session, g
from werkzeug.security import check_password_hash
# from flask_security import login_required

from .UsuarioQueries import UsuarioQueries
from ..config import USUARIO_ADMIN


auth = Blueprint('auth', __name__)


@auth.before_request
def before_request():
    if 'id' in session:
        model = UsuarioQueries()
        id = session['id']
        usuario = model.consultar_cliente_por_id(id)
        g.user = usuario


@auth.route('/', methods=['GET'])
def index():
    return render_template('landing_page.html')


@auth.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    passsword = request.form.get('password')

    model = UsuarioQueries()
    usuario = model.consultar_por_email(email)

    if not usuario or not check_password_hash(usuario.password, passsword):
        flash('El usuario y/o la contraseña son incorrectos')
        return redirect(url_for('auth.login_get'))

    session['id'] = usuario.id
    g.user = usuario
    g.rol = usuario.idRol
    mensaje = 'Bienvenido ' + usuario.nombre

    if(usuario.idRol == 2):
        flash(mensaje)
        return redirect('/productos')

    if(usuario.idRol == 3):
        flash(mensaje)
        return redirect(url_for('administrativo.consultar_ventas_get'))

    if(usuario.idRol == 1):
        flash(mensaje)
        return redirect(url_for('cliente.miInformacion'))


@auth.route('/signup', methods=['GET'])
def signup_get():
    return render_template('/signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    # TODO Verificar form
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


@auth.route('/logout')
def logout():
    flash('Se cerró la sesión exitosamente')
    session.pop('id', None)
    g.user = None
    g.rol = None
    return redirect(url_for('auth.login_get'))
