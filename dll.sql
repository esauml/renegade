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
    activo      TINYINT(1) DEFAULT 1
);



CREATE TABLE IF NOT EXISTS Estructura (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    idProducto     INT,
    idMateriaPrima INT,
    cantidad       INT,
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