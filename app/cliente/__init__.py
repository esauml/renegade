
from flask import Blueprint, render_template, request, flash, g, session
from .clienteQueries import ClienteQueries
from ..site import UsuarioQueries, Rol

cliente = Blueprint('cliente', __name__)

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
        return render_template('login.html') 
        

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

@cliente.route("/perfil", methods=['GET'])
def profile_get():   
    cliente_queries = ClienteQueries()
    cliente = cliente_queries.consultar_perfil(g.user.id)
    
    if cliente == None:
        flash('Ocurrió un error, favor de inciar sesión nuevamente.')
        return render_template('login.html') 
    
    return render_template('/cliente/perfil.html', cliente = cliente)

@cliente.route("/actualizar-perfil", methods=['GET'])
def profile_post():   
    #TODO Agregar logica
    return ''