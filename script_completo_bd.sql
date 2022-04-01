DROP DATABASE IF EXISTS renegade;
CREATE DATABASE IF NOT EXISTS renegade;

USE renegade;

CREATE TABLE IF NOT EXISTS Rol (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(50),
    description VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Usuario (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    nombres   VARCHAR(50),
    apellidos VARCHAR(50),
    correo    VARCHAR(100) UNIQUE,
    password  VARCHAR(255),
    active    TINYINT(1) DEFAULT 0,
    idRol     INT        DEFAULT 1,
    FOREIGN KEY (idRol) REFERENCES Rol (id)
);

CREATE TABLE IF NOT EXISTS Proveedor (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    nombre   VARCHAR(50), -- Nombre de la empresa
    contacto VARCHAR(50), -- Nombre de la persona (Contacto persona)
    telefono VARCHAR(20),
    correo   VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS MateriaPrima (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nombre      VARCHAR(50),
    descripcion TEXT,
    cantidad    INT,
    unidad      VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Compra (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    folio       VARCHAR(50) UNIQUE,
    idProveedor INT,
    fechaCompra DATE,
    FOREIGN KEY (idProveedor) REFERENCES Proveedor (id)
);


CREATE TABLE IF NOT EXISTS StockMateriaPrima (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    cantidad       FLOAT,
    idMateriaPrima INT,
    idOrdenCompra  INT,
    FOREIGN KEY (idMateriaPrima) REFERENCES MateriaPrima (id),
    FOREIGN KEY (idOrdenCompra) REFERENCES Compra (id)
);

CREATE TABLE IF NOT EXISTS CompraStockMateria (
    idOrdenCompra  INT,
    idMateriaPrima INT,
    cantidad       INT,
    costo          FLOAT,
    PRIMARY KEY (idOrdenCompra, idMateriaPrima),
    FOREIGN KEY (idMateriaPrima) REFERENCES MateriaPrima (id),
    FOREIGN KEY (idOrdenCompra) REFERENCES Compra (id)
);


CREATE TABLE IF NOT EXISTS Producto (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nombre      VARCHAR(50),
    descripcion TEXT,
    precio      FLOAT,
    talla       VARCHAR(50),
    stock       INT DEFAULT 0,
    image_url   TEXT,
    activo      tinyint
);



CREATE TABLE IF NOT EXISTS Estructura (
    id             int PRIMARY KEY AUTO_INCREMENT,
    idProducto     INT,
    idMateriaPrima INT,
    descripcion    VARCHAR(50),
    cantidad       FLOAT,
    FOREIGN KEY (idProducto) REFERENCES Producto (id),
    FOREIGN KEY (idMateriaPrima) REFERENCES MateriaPrima (id)
);

CREATE TABLE IF NOT EXISTS Carrito (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    status    TINYINT(1) DEFAULT 0, -- 0 -> Activo | 1 -> Vendido
    idUsuario INT,
    FOREIGN KEY (idUsuario) REFERENCES Usuario (id)
);

CREATE TABLE IF NOT EXISTS ProductoCarrito (
    idProducto INT,
    idCarrito  INT,
    cantidad   INT,
    precio     FLOAT,
    PRIMARY KEY (idProducto, idCarrito),
    FOREIGN KEY (idProducto) REFERENCES Producto (id),
    FOREIGN KEY (idCarrito) REFERENCES Carrito (id)
);

CREATE TABLE IF NOT EXISTS Venta (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    folio     VARCHAR(50) UNIQUE,
    total     FLOAT,
    fecha     DATETIME,
    idCarrito INT,
    FOREIGN KEY (idCarrito) REFERENCES Carrito (id)
);

CREATE TABLE IF NOT EXISTS MaterialUsado (
    idProducto          INT,
    idStockMateriaPrima INT,
    cantidad            INT,
    PRIMARY KEY (idProducto, idStockMateriaPrima),
    FOREIGN KEY (idProducto) REFERENCES Producto (id),
    FOREIGN KEY (idStockMateriaPrima) REFERENCES StockMateriaPrima (id)
);


-- Esta tabla es para resurtir en la aplicación los productos, el administrador gestiona la falta de productos
CREATE TABLE IF NOT EXISTS Pedido (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    cantidad    INT DEFAULT 0,
    idProducto  INT,
    idUsuario   INT,
    fechaPedido DATE,
    FOREIGN KEY (idProducto) REFERENCES Producto (id),
    FOREIGN KEY (idUsuario) REFERENCES Usuario (id)
);

-------------------------------------------------------------------------------------------------
-- Vistas

--------------------------------------------------------------------------------------------------

drop view if exists vista_stock_materia;
create view vista_stock_materia as
(
select m.id,
       m.nombre,
       m.descripcion,
       concat(stk.cantidad, ' ', m.unidad) as stock,
       com.folio,
       com.fechaCompra,
       p.nombre                            as Proveedor

from StockMateriaPrima as stk
         inner join MateriaPrima as m on stk.idMateriaPrima = m.id
         inner join Compra as com on com.id = stk.idOrdenCompra
         inner join CompraStockMateria as comStk on comStk.idMateriaPrima = m.id
         inner join Proveedor as p on com.idProveedor = p.id
    );

-------------------------------------------------------------------------------------------------
-- Inserts

--------------------------------------------------------------------------------------------------



-- INSERCIONES PROVEEDOR --
insert into proveedor (nombre, contacto, telefono, correo)
values ('proveedorTela', 'agenteProveedorTela', '477-000-00-00', 'correo@proveedor'),
       ('proveedorTela2', 'agenteProveedorTela2', '477-000-00-00', 'correo1@proveedor'),
       ('proveedorTela3', 'agenteProveedorTela3', '477-000-00-00', 'correo2@proveedor'),
       ('proveedorTela4', 'agenteProveedorTela4', '477-000-00-00', 'correo3@proveedor');

-- INSERCIONES COMPRA --
insert into compra (folio, idProveedor, fechaCompra)
values ('00001', 1, '2022/03/30');
insert into compra (folio, idProveedor, fechaCompra)
values ('00002', 1, '2022/03/30');


-- INSERSCIONES CATALOGO MATERIA PRIMA --
insert into MateriaPrima (nombre, descripcion, cantidad, unidad)
values ('Rollo de tela negra', 'Tela para el diseño de playeras', 50, 'metros');
insert into MateriaPrima (nombre, descripcion, cantidad, unidad)
values ('Rollo de tela blanca', 'Tela para el diseño de playeras', 50, 'metros');


-- INSERCIONES STOCKCOMPRA --
insert into CompraStockMateria (idOrdenCompra, idMateriaPrima, Cantidad, costo)
values (1, 1, 1, 250.00);
insert into CompraStockMateria (idOrdenCompra, idMateriaPrima, Cantidad, costo)
values (1, 2, 3, 255.00);

-- INSERCIONES STOCKMATERIA -- 
insert into StockMateriaPrima (cantidad, idMateriaPrima, idOrdenCompra)
values (50, 1, 1);
INSERT INTO StockMateriaPrima (cantidad, idMateriaPrima, idOrdenCompra)
values (50, 2, 1);
INSERT INTO StockMateriaPrima (cantidad, idMateriaPrima, idOrdenCompra)
values (50, 2, 1);
INSERT INTO StockMateriaPrima (cantidad, idMateriaPrima, idOrdenCompra)
values (50, 2, 1);

--INSERCIONES DE ROL--
INSERT INTO Rol(name, description)
VALUES ('cliente', 'Rol designado para los usuarios finales'),
       ('administrador', 'Rol designado para los administradores del sistema'),
       ('administrativo', 'Rol designado para los administrativos del sistema');

-- INSERCIONES USUARIO--
-- Las contrasenias son password --
INSERT INTO usuario(nombres, apellidos, correo, password, active, idRol)
VALUES ('Nombre de administrador', 'Apellidos', 'administrador@gmail.com',
        'sha256$1Ftzf32tZ0QCcdHj$0ebc4d9c6e18261e08f17a5fbc5572d7d6f3a75ea692dee2d59e2c1e2dbdb197', 1, 2),
       ('Nombre de administrativo', 'Apellidos', 'administrativo@gmail.com',
        'sha256$1Ftzf32tZ0QCcdHj$0ebc4d9c6e18261e08f17a5fbc5572d7d6f3a75ea692dee2d59e2c1e2dbdb197', 1, 3),
       ('Nombre de cliente', 'Apellidos', 'cliente@gmail.com',
        'sha256$1Ftzf32tZ0QCcdHj$0ebc4d9c6e18261e08f17a5fbc5572d7d6f3a75ea692dee2d59e2c1e2dbdb197', 1, 1);