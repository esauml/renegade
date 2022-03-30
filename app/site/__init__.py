from flask import Blueprint, render_template, request, flash, redirect, url_for, session, g
from werkzeug.security import check_password_hash
from flask_security import login_required

from .model_user import ModelUser
from .rol import Rol
from ..config import USUARIO_ADMIN


auth = Blueprint('auth', __name__)


@auth.before_request
def before_request():
    if 'id' in session:
        model = ModelUser()
        rol_obj = rol.Rol()
        id = session['id']
        usuario = model.consultar_cliente_por_id(id)
        roles = rol_obj.obtener_roles_por_usuario_id(id)
        g.user = usuario
        g.rol = roles[0]


@auth.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    passsword = request.form.get('password')

    model = ModelUser()
    usuario = model.consultar_por_email(email)

    if not usuario or not check_password_hash(usuario.password, passsword):
        flash('El usuario y/o la contraseña son incorrectos')
        return redirect(url_for('auth.login_get'))

    rol_obj = rol.Rol()
    roles = rol_obj.obtener_roles_por_usuario_id(usuario.id)
    session['id'] = usuario.id  
    print(usuario)
    mensaje = 'Bienvenido ' + usuario.nombre
    if(roles[0] == 'administrador'):
        flash(mensaje)
        return render_template('/adm/index.html')

    if(roles[0] == 'administrativo'):
        flash(mensaje)
        return render_template('/adm/index.html')

    if(roles[0] == 'cliente'):
        flash(mensaje)
        return render_template('/landing_page.html')


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

    model = ModelUser()
    usuario_email = model.consultar_por_email(email)

    if usuario_email:
        flash('Ese correo electrónico ya existe')
        return redirect(url_for('auth.signup_get'))

    model.registro_usuario(USUARIO_ADMIN, nombre, apellidos, email, password)
    usuario = model.consultar_por_email(email)

    rol_obj = rol.Rol()
    rol_obj.agregar_rol_cliente_por_id(USUARIO_ADMIN, usuario.id)

    return redirect(url_for('auth.login_get'))


@auth.route('/logout')
@login_required
def logout():
    session.pop('id', None)
    g.user = None
    g.rol = None
    return redirect(url_for('index'))
