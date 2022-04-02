

from pydoc import cli
from flask import Blueprint, redirect, render_template, request, flash, g, session, url_for
from .clienteQueries import Cliente as Query
from ..site import UsuarioQueries
from ..config import USUARIO_CLIENTE
import logging
from flask import current_app as app

# routes import
from .RoutesClienteCarrito import cliente_carrito_blueprint as carrito
from .RoutesClienteProductos import cliente_productos_blueprint as producto

cliente = Blueprint('cliente', __name__)

# routes subscribe
cliente.register_blueprint(carrito)
cliente.register_blueprint(producto)


@cliente.before_request
def before_request_cliente():
    if 'id' in session:
        model = UsuarioQueries()
        id = session['id']
        usuario = model.consultar_cliente_por_id(id)
        if usuario.idRol == 2 or usuario.idRol == 3:
            flash('No cuentas con permisos para consultar este módulo')
            return render_template('/login.html')
        g.user = usuario
    else:
        flash('Es necesario inicar sesión para consultar este módulo')
        return render_template('login.html')


@cliente.route("/index", methods=["GET"])
def index():
    return render_template('/landing_page.html')


@cliente.route("/mis-compras", methods=['GET'])
def consultar_mis_compras():
    queries=Query()
    carritos = queries.consulta_mis_ventas(g.user.id)
    return render_template("/cliente/miscompras.html",carritos=carritos)

@cliente.route("/detalle-carrito-usuario/<id>", methods=['GET'])
def detalle_carrito_usuario(id):
    queries=Query()
    productos = queries.detalle_consulta_mis_ventas(id)
    return render_template("cliente/detalle-carrito.html",productos=productos)


@cliente.route('/mi-informacion')
def miInformacion():
    return render_template("/cliente/infoUsuario.html")


@cliente.route('/actualizar-cliente', methods=["POST"])
def actualizar_Cliente():
    queries = Query()
    queries.actualizarUsuario(nombre=request.form.get("nombres"), apellidos=request.form.get("apellidos"),
                                        email=request.form.get("correo"),
                                        id=request.form.get("idCliente"))
    return redirect(url_for('cliente.miInformacion'))


@cliente.route("/perfil", methods=['GET'])
def profile_get():
    cliente_queries = Query()
    cliente = cliente_queries.consultar_perfil(g.user.id)

    if cliente == None:
        flash('Ocurrió un error, favor de inciar sesión nuevamente.')
        return render_template('login.html')

    return render_template('/cliente/perfil.html', cliente=cliente)


@cliente.route("/mi-carrito", methods=['GET'])
def profile_post():
    return render_template("/cliente/micarrito.html", productos=[])


@cliente.route("/generar-venta", methods=['POST'])
def generar_venta_post():
    queries = Query()
    puede_comprar = queries.puede_comprar(g.user.id)

    if puede_comprar:
        queries.generar_venta(g.user.id)
        flash('Su compra se registro exitosamente.')
        return render_template("/cliente/micarrito.html", productos=[])
    
    flash('Uno o varios productos exceden el máximo de nuestros inventarios.')
    app.logger.debug('Se genera nueva venta')
    return render_template("/cliente/micarrito.html", productos=[])

