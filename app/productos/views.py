
from multiprocessing import context
from flask import render_template, session, redirect,flash,url_for
from app.productos.materia_prima import MateriaPrima
from . import Productos
from ..config import USUARIO_ADMIN


@Productos.route('/getAllMateria', methods=['GET'])
def getAllMateria():
    try:
        materia=MateriaPrima()
        materias = materia.consultar_materias_primas(USUARIO_ADMIN);
        
        print (materias)
        return render_template("adm/administrador/materias.html", materias=materias)
    except Exception as e:
        # TODO What to do when couldn't handle DB operation
        print("Exception: ", e)
        raise e
    

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