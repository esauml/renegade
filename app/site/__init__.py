from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash
from flask_security.utils import login_user, logout_user
from flask_security import login_required

from .usuario import Usuario
from .rol import Rol
from ..config import USUARIO_ADMIN

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    passsword = request.form.get('password')

    usuario_obj = usuario.Usuario(False, False, False)
    usuario_email = usuario_obj.consultar_por_email(USUARIO_ADMIN, email)

    if not usuario_email or not check_password_hash(usuario_email[4], passsword):
        flash('El usuario y/o la contraseña son incorrectos')
        return redirect(url_for('auth.login'))

    login_user(usuario_email)
    # TODO Hacer un if para verificar el tipo de usuario y redirigirlo a su pagina respectiva o separar los login. 
    return render_template('/index.html')


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

    usuario_obj = usuario.Usuario()
    usuario_email = usuario_obj.consultar_por_email(USUARIO_ADMIN, email)

    if usuario_email:
        flash('Ese correo electrónico ya existe')
        return redirect(url_for('auth.signup_get'))
    
    usuario_obj.registro_usuario(USUARIO_ADMIN, nombre, apellidos, email, password)
    usuario_email = usuario_obj.consultar_por_email(USUARIO_ADMIN, email)

    rol_obj = rol.Rol()
    rol_obj.agregar_rol_cliente_por_id(USUARIO_ADMIN, usuario_email[0])

    return redirect(url_for('auth.login_get'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
