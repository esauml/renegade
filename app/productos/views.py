
from multiprocessing import context
from flask import render_template, session, redirect, flash, url_for, g
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
        if usuario.idRol == 1:
            flash('No cuentas con permisos para consultar este módulo')
            return render_template('login.html')
        g.user = usuario
    else:
        flash('Es necesario inicar sesión para consultar este módulo')
        return render_template('login.html')


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
