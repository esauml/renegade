
from flask import Blueprint, g, session, flash, render_template
from ..cliente.clienteQueries import Cliente
from ..site import UsuarioQueries, Rol

administrativo = Blueprint('administrativo', __name__)

@administrativo.before_request
def before_request_administrativo():
    if 'id' in session:
        usuario_queries = UsuarioQueries()
        rol_obj = Rol()
        id = session['id']
        usuario = usuario_queries.consultar_cliente_por_id(id)
        roles = rol_obj.obtener_roles_por_usuario_id(id)
        g.user = usuario
        g.rol = roles[0]
        if g.rol == 'administrador' or g.rol == 'cliente':
            flash('El perfil no cuenta con permisos para consultar esta página.')
            return render_template('login.html')  
    else:
        flash('Es necesario inciar sesión previamente.')
        return render_template('login.html') 

@administrativo.route("/consultar-ventas", methods=['GET'])
#@roles_required('administrativo')
def consultar_ventas_get():
    return 0

@administrativo.route("/consultar-rendimiento", methods=['GET'])
#@roles_required('administrativo')
def consultar_rendimiento_get():
    # calculo de rendimiento
    return 0