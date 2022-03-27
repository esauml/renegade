DROP DATABASE IF EXISTS renegade;
CREATE DATABASE renegade;
USE renegade;

CREATE TABLE producto
(
    id          INT PRIMARY KEY AUTO_INCREMENT,
    nombre      VARCHAR(250) NOT NULL UNIQUE,
    descripcion VARCHAR(250),
    precio      DOUBLE       NOT NULL DEFAULT 0.0,
    activo      BOOLEAN               DEFAULT 1
);

CREATE TABLE materia_prima
(
    id       INT PRIMARY KEY AUTO_INCREMENT,
    nombre   VARCHAR(250) NOT NULL UNIQUE,
    costo    DOUBLE       NOT NULL DEFAULT 0.0,
    en_stock INT          NOT NULL DEFAULT 0
);


CREATE TABLE producto_materia_prima
(
    id               INT PRIMARY KEY AUTO_INCREMENT,
    producto_id      INT NOT NULL,
    mataria_prima_id INT NOT NULL,
    cantidad         INT NOT NULL DEFAULT 1,
    FOREIGN KEY (producto_id) REFERENCES producto (id),
    FOREIGN KEY (mataria_prima_id) REFERENCES materia_prima (id)
);

CREATE TABLE usuario
(
    id        INT PRIMARY KEY AUTO_INCREMENT,
    nombre    VARCHAR(250) NOT NULL,
    apellidos VARCHAR(250) NOT NULL,
    email     VARCHAR(250) NOT NULL UNIQUE,
    password  VARCHAR(250) NOT NULL,
    activo    BOOLEAN DEFAULT 1
);


CREATE TABLE rol
(
    id     INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(250) NOT NULL
);

CREATE TABLE usuario_rol
(
    id         INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    rol_id     INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuario (id),
    FOREIGN KEY (rol_id) REFERENCES rol (id)
);

INSERT INTO producto(nombre, descripcion, precio, activo)
VALUES ('Ejemplo 1', 'Descripcion 1', 10.50, 1),
       ('Ejemplo 2', 'Descripcion 2', 10.50, 1);

INSERT INTO materia_prima (nombre, costo, en_stock)
VALUES ('Botones', 0.5, 10),
       ('Algo mas', 1.0, 5);

INSERT INTO producto_materia_prima(producto_id, mataria_prima_id, cantidad)
VALUES (1, 1, 2),
       (1, 2, 3),
       (2, 2, 1);


INSERT INTO usuario(nombre, apellidos, email, password, activo)
VALUES ('Cliente', 'cliente', 'cliente@gmail.com', 'password', 1),
       ('Administrador', 'administrador', 'administrador@gmail.com', 'password', 1),
       ('Administrativo', 'administrativo', 'administrativo@gmail.com', 'password', 1);

INSERT INTO rol (nombre)
VALUES ('administrador'),
       ('administrativo'),
       ('cliente');

INSERT INTO usuario_rol(usuario_id, rol_id)
VALUES (1, 3),
       (2, 1),
       (3, 2);

SELECT prod.id, prod.nombre, descripcion, precio, activo, mp.nombre, pmp.cantidad
FROM producto prod
         INNER JOIN producto_materia_prima pmp ON prod.id = pmp.producto_id
         INNER JOIN materia_prima mp on pmp.mataria_prima_id = mp.id
WHERE prod.id = 1;


SELECT * FROM usuario;