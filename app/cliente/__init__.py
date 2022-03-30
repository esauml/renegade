
from flask import Blueprint, redirect, render_template, request, flash, url_for
from .ClienteQueries import Cliente as Query
from ..config import USUARIO_CLIENTE

cliente = Blueprint('cliente', __name__)

@cliente.route("/carrito-compras", methods=['GET'])
#@roles_required('cliente')
def consultar_ventas_get():
    # current_user()
    # consulta de carrito en BD
    return 0

@cliente.route("/agregar-producto-carrito", methods=['POST'])
#@roles_required('cliente')
def agregar_producto_carrito_post():
    # id producto
    #cantidad
    return 0

@cliente.route("/index",methods=["GET"])
def index():
    return render_template("cliente/index.html")

@cliente.route('/mi-informacion')
def miInformacion():
    queries=Query()
    try:
        cliente=queries.consultarCliente(tipo_usuario=USUARIO_CLIENTE,id=1)
        return render_template("cliente/infoUsuario.html",cliente=cliente[0])
    except Exception as e:
        raise e
        return render_template("cliente/infoUsuario.html",expetion=e)
    
@cliente.route('/actualizar-cliente', methods=["POST"])
def actualizar_Cliente():
    queries=Query()
    try:
        cliente=queries.actualizarUsuario(nombre=request.form.get("nombres"),apellidos=request.form.get("apellidos"),
                                          email=request.form.get("correo"),password=request.form.get("contraseña"),
                                          id=request.form.get("idCliente"),tipo_usuario=USUARIO_CLIENTE)
        return redirect(url_for('cliente.miInformacion'))
        
    except Exception as e:
        raise e
        return render_template("cliente/infoUsuario.html",expetion=e)
    