

from flask import Blueprint, redirect, render_template, request, flash, g, session, url_for
from .clienteQueries import Cliente as Query
from ..site import UsuarioQueries, Rol
from ..config import USUARIO_CLIENTE

cliente = Blueprint('cliente', __name__)
'''
@cliente.before_request
def before_request_cliente():
    if 'id' in session:
        usuario_queries = UsuarioQueries()
        rol_obj = Rol()
        id = session['id']
        usuario = usuario_queries.consultar_cliente_por_id(id)
        roles = rol_obj.obtener_roles_por_usuario_id(id)
        g.user = usuario
        g.rol = roles[0]
        if g.rol == 'administrador' or g.rol == 'administrativo':
            flash('El perfil no cuenta con permisos para consultar esta página.')
            return render_template('login.html')  
    else:
        flash('Es necesario inciar sesión previamente.')
        return render_template('login.html') '''
        

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
    

@cliente.route("/perfil", methods=['GET'])
def profile_get():   
    cliente_queries = Query()
    cliente = cliente_queries.consultar_perfil(g.user.id)
    
    if cliente == None:
        flash('Ocurrió un error, favor de inciar sesión nuevamente.')
        return render_template('login.html') 
    
    return render_template('/cliente/perfil.html', cliente = cliente)

@cliente.route("/mi-carrito", methods=['GET'])
def profile_post():   
    
    return render_template("/cliente/micarrito.html")
