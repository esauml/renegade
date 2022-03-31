
from multiprocessing import context
from flask import render_template, session, redirect, flash, url_for, g, request
from app.productos.materia_prima import MateriaPrima
from . import Productos
from ..config import USUARIO_ADMIN
from ..site import UsuarioQueries


@Productos.before_request
def before_request_administrador():
    if 'id' in session:
        model = UsuarioQueries()
        id = session['id']
        usuario = model.consultar_cliente_por_id(id)
        g.user = usuario


@Productos.route('/getAllMateria', methods=['GET'])
def getAllMateria():
    materia = MateriaPrima()
    materias = materia.consultar_materias_primas(USUARIO_ADMIN)

    print(materias)
    return render_template("adm/administrador/materias.html", materias=materias)


@Productos.route("/detalle-materia/<id>", methods=['GET'])
# @roles_required('administrador')
def consultar_producto_get(id):
    # inputs
    materia_id = id
    # init query handler
    queries = MateriaPrima()
    print(materia_id)
    # consulta
    try:
        materia = queries.consultar_materia_prima_id(USUARIO_ADMIN, materia_id)

        return render_template('adm/administrador/detalle-materia.html', materia=materia)
    except Exception as e:
        raise e

@Productos.route("/editar-materia", methods=['POST'])
def editar_producto_post():
    # TODO Validar formulario
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    id = request.form.get('id')

    queries = MateriaPrima()
    queries.actualizar_materia(USUARIO_ADMIN, nombre, descripcion,  id)
    return redirect(url_for('productos.getAllMateria'))



@Productos.route("/agregar-materia", methods=['POST'])
def agregar_materia():
    return render_template('adm/administrador/agregar-materia.html')

@Productos.route("/guardar-materia", methods=['POST'])
def guardar():
    # TODO Validar formulario
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    cantidad = request.form.get('cantidad')
    unidad = request.form.get('unidad')

    queries = MateriaPrima()
    queries.guardar_materia(USUARIO_ADMIN, nombre, descripcion, cantidad, unidad)
    return redirect(url_for('productos.getAllMateria'))