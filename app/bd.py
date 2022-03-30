import pymysql
from .config import servidor_db, nombre_bd, \
    usuario_conexion_admin, contrasenia_conexion_admin, \
    usuario_conexion_administrativo, contrasenia_conexion_administrativo, \
    usuario_conexion_cliente, contrasenia_conexion_cliente


def obtener_conexion(tipo_usuario):
    if(tipo_usuario == 1):
        return obtener_conexion_administrador()

    if(tipo_usuario == 2):
        return obtener_conexion_administrativo()

    return obtener_conexion_cliente()


def obtener_conexion_administrador():
    return pymysql.connect(
        host=servidor_db,
        user=usuario_conexion_admin,
        password=contrasenia_conexion_admin,
        db=nombre_bd
    )


def obtener_conexion_administrativo():
    return pymysql.connect(
        host=servidor_db,
        user=usuario_conexion_admin,
        password=contrasenia_conexion_admin,
        db=nombre_bd
    )


def obtener_conexion_cliente():
    return pymysql.connect(
        host=servidor_db,
        user=usuario_conexion_admin,
        password=contrasenia_conexion_admin,
        db=nombre_bd
    )
