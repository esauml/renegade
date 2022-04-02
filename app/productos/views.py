
from multiprocessing import context
from flask import render_template, session, redirect, flash, url_for, g, request
from app.productos.materia_prima import MateriaPrima
from app.productos.compras import Compras
from . import Productos
from ..site import UsuarioQueries
from datetime import date
<<<<<<< HEAD
mateSelect = {}
mateSelect['insumos'] = []


=======
mateSelect={}
mateSelect['insumos']=[]
materiaSel={}
materiaSel['insumos']=[]
>>>>>>> oscar
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
    materias = materia.consultar_materias_primas()

    print(materias)
    return render_template("adm/administrador/materias.html", materias=materias)


@Productos.route("/detalle-materia/<id>", methods=['GET'])
def consultar_producto_get(id):
    # inputs
    materia_id = id
    # init query handler
    queries = MateriaPrima()
    print(materia_id)
    # consulta
    try:
        materia = queries.consultar_materia_prima_id(materia_id)

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
    queries.actualizar_materia(nombre, descripcion,  id)
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
    queries.guardar_materia(nombre, descripcion, cantidad, unidad)
    return redirect(url_for('productos.getAllMateria'))


@Productos.route('/compras-nosurtidas', methods=['GET'])
def getComprasNo():
    compra = Compras()
    compras = compra.consultar_compras_nosurtidas(USUARIO_ADMIN)
    
    print(compras)
    return render_template("adm/administrador/compras-no-surtidas.html", compras=compras)


@Productos.route('/getCompras', methods=['GET'])
def getCompras():
    compra = Compras()
    compras = compra.consultar_compras()

    print(compras)
    return render_template("adm/administrador/compras.html", compras=compras)


    
@Productos.route('/compra-nosurtida/<id>', methods=['GET'])
def compra_nosurtida(id):
    # inputs
    compra_id = id
    # init query handler
    queries = Compras()
    print(compra_id)
    # consulta
    try:
        compra = queries.consultar_compranosurtida_id(USUARIO_ADMIN, compra_id)
        materia=queries.consultar_materias_compranosurtidas(USUARIO_ADMIN, compra_id)
        print (materia)
        return render_template('adm/administrador/detalle-compra-nosurtida.html', compra=compra,materias=materia)
    except Exception as e:
        raise e
    

@Productos.route("/detalle-compra/<id>", methods=['GET'])
def consultar_compra_get(id):
    # inputs
    compra_id = id
    # init query handler
    queries = Compras()
    print(compra_id)
    # consulta
    try:
        compra = queries.consultar_compra_id(compra_id)
        materia = queries.consultar_materias_compra(compra_id)
        print(materia)
        return render_template('adm/administrador/detalle-compra.html', compra=compra, materias=materia)
    except Exception as e:
        raise e

<<<<<<< HEAD

@Productos.route("/cargar-agregar-compra", methods=['POST', 'GET'])
=======
@Productos.route('/cargar-agregar-compra', methods=['POST','GET'])
>>>>>>> oscar
def cargar_agregar_compra():
    if request.method == 'POST':
        queries = Compras()
        insumo = request.form.get('materias')
        cantidad = request.form.get('cantidad')
        materia = queries.consultar_materia_id(insumo)
        mateSelect['insumos'].append({
            'id': insumo,
            'insumo': materia[1],
            'cant': materia[3],
            'unidad': materia[4],
            'cantidad': cantidad,
            'costo': materia[5]
        })

        folio = queries.asignarFolio()
        fecha = date.today()
        proveedores = queries.consultar_proveedor_select()
        materias = queries.consultar_materia_select()
        return render_template('adm/administrador/agregar-compra.html',  folio=folio, fecha=fecha,
                               materias=materias, mateSelect=mateSelect['insumos'], proveedores=proveedores)
    else:
        queries = Compras()
        folio = queries.asignarFolio()
        fecha = date.today()

        materias = queries.consultar_materia_select()
        proveedores = queries.consultar_proveedor_select()
        return render_template('adm/administrador/agregar-compra.html', folio=folio,
                               fecha=fecha, materias=materias, mateSelect=mateSelect['insumos'], proveedores=proveedores)

<<<<<<< HEAD

@Productos.route('/quitar-materia', methods=['POST'])
def quitar_materia():
    id = int(request.form.get('iterador'))

    mateSelect['insumos'].pop(id)
    return redirect(url_for('productos.cargar_agregar_compra'))
=======
>>>>>>> oscar

        
@Productos.route('/guardarArribo', methods=['POST'])
def guardar_arribo():
    compra = Compras()
    folio = request.form.get('folio')
    fecha = request.form.get('fecha')
    proveedor = request.form.get('proveedores')
    listaMaterias = mateSelect['insumos']
    try:
        print (folio, fecha)
        compra.insertar_compra(tipo_usuario=USUARIO_ADMIN, folio=folio, fecha=fecha, proveedor=proveedor, listaMaterias=listaMaterias)
        mateSelect['insumos']=[]
        return redirect(url_for('productos.getCompras'))
    except Exception as e:
        raise e
    
    
    
    