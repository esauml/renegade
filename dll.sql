DROP DATABASE IF EXISTS renegade;
CREATE DATABASE IF NOT EXISTS renegade;

USE renegade;

CREATE TABLE IF NOT EXISTS Usuario
(
    id           INT AUTO_INCREMENT PRIMARY KEY,
    nombres      VARCHAR(50)  NOT NULL,
    apellidos    VARCHAR(50)  NOT NULL,
    correo       VARCHAR(100) NOT NULL UNIQUE,
    password     VARCHAR(255) NOT NULL,
    active       TINYINT(1) DEFAULT 0,
    confirmed_at DATETIME
);

CREATE TABLE IF NOT EXISTS Rol
(
    id          INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(50) NOT NULL,
    description VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS Rol_Usuario
(
    idUsuario INT,
    idRol     INT,
    PRIMARY KEY (idUsuario, idRol),
    FOREIGN KEY (idUsuario) REFERENCES Usuario (id),
    FOREIGN KEY (idRol) REFERENCES Rol (id)
);

CREATE TABLE IF NOT EXISTS Proveedor
(
    id       INT AUTO_INCREMENT PRIMARY KEY,
    nombre   VARCHAR(50)  NOT NULL, -- Nombre de la empresa
    contacto VARCHAR(50)  NOT NULL, -- Nombre de la persona (Contacto persona)
    telefono VARCHAR(20)  NOT NULL,
    correo   VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS MateriaPrima
(
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nombre      VARCHAR(50) NOT NULL,
    descripcion TEXT        NOT NULL,
    costo       FLOAT       NOT NULL,
    stock       INT         NOT NULL,
    idProveedor INT         NOT NULL,
    FOREIGN KEY (idProveedor) REFERENCES Proveedor (id)
);

CREATE TABLE IF NOT EXISTS Producto
(
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nombre      VARCHAR(50) NOT NULL,
    descripcion TEXT        NOT NULL,
    activo      TINYINT
);

CREATE TABLE IF NOT EXISTS Estructura
(
    id             INT AUTO_INCREMENT PRIMARY KEY,
    idProducto     INT NOT NULL,
    idMateriaPrima INT NOT NULL,
    cantidad       INT NOT NULL,
    FOREIGN KEY (idProducto) REFERENCES Producto (id),
    FOREIGN KEY (idMateriaPrima) REFERENCES MateriaPrima (id)
);

CREATE TABLE IF NOT EXISTS Carrito
(
    id        INT AUTO_INCREMENT PRIMARY KEY,
    status    TINYINT(1) DEFAULT 0, -- 0 -> Activo | 1 -> Vendido
    idUsuario INT NOT NULL,
    FOREIGN KEY (idUsuario) REFERENCES Usuario (id)
);

CREATE TABLE IF NOT EXISTS ProductoCarrito
(
    idProducto INT NOT NULL,
    idCarrito  INT NOT NULL,
    cantidad   INT,
    PRIMARY KEY (idProducto, idCarrito),
    FOREIGN KEY (idProducto) REFERENCES Producto (id),
    FOREIGN KEY (idCarrito) REFERENCES Carrito (id)
);

CREATE TABLE IF NOT EXISTS Venta
(
    id        INT AUTO_INCREMENT PRIMARY KEY,
    total     TINYINT(1) DEFAULT 0,
    fecha     DATETIME NOT NULL,
    idCarrito INT      NOT NULL,
    FOREIGN KEY (idCarrito) REFERENCES Carrito (id)
);

CREATE TABLE IF NOT EXISTS Log
(
    id             INT AUTO_INCREMENT PRIMARY KEY,
    cantidad       INT NOT NULL,
    idProducto     INT NOT NULL,
    idMateriaPrima INT,
    FOREIGN KEY (idProducto) REFERENCES Producto (id),
    FOREIGN KEY (idMateriaPrima) REFERENCES MateriaPrima (id)
);

CREATE TABLE IF NOT EXISTS Pedido
(
    id           INT AUTO_INCREMENT PRIMARY KEY,
    cantidad     INT DEFAULT 0,
    idProducto   INT  NOT NULL,
    idUsuario    INT  NOT NULL,
    fechaEntrega DATE NOT NULL,
    FOREIGN KEY (idProducto) REFERENCES Producto (id),
    FOREIGN KEY (idUsuario) REFERENCES Usuario (id)
);

INSERT INTO Rol (name, description) VALUES ('administrador', 'Administrador'), ('administrativo', 'Administrativo'), ('Cliente', 'cliente');