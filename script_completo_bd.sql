DROP DATABASE IF EXISTS renegade;
CREATE DATABASE IF NOT EXISTS renegade;

USE renegade;

-- TABLAS --
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
    idRol     INT DEFAULT 1,
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
    cant_min    INT DEFAULT 1,
    cant_max    INT DEFAULT 10,
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
    cant_min    INT DEFAULT 1,
    cant_max    INT DEFAULT 10,
    stock       INT DEFAULT 5,
    image_url   TEXT,
    activo tinyint
);


CREATE TABLE IF NOT EXISTS Estructura (
    id INT PRIMARY KEY AUTO_INCREMENT,
    idProducto     INT,
    idMateriaPrima INT,
    cantidad       INT,
    descripcion    VARCHAR(50),
    FOREIGN KEY (idProducto) REFERENCES Producto (id),
    FOREIGN KEY (idMateriaPrima) REFERENCES MateriaPrima (id)
);

CREATE TABLE IF NOT EXISTS Carrito (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    status    TINYINT(1) DEFAULT 1,
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


-- TODO Esta tabla es para resurtir en la aplicación los productos, el administrador gestiona la falta de productos
CREATE TABLE IF NOT EXISTS Pedido (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    cantidad    INT DEFAULT 0,
    idProducto  INT,
    idUsuario   INT,
    fechaPedido DATE,
    FOREIGN KEY (idProducto) REFERENCES Producto (id),
    FOREIGN KEY (idUsuario) REFERENCES Usuario (id)
);

-- VISTAS --
drop view if exists vista_stock_materia;
create view vista_stock_materia as (
	select
	m.id,
	m.nombre,
    m.descripcion,
    concat(stk.cantidad,' ',m.unidad) as stock,
    com.folio,
    com.fechaCompra,
    p.nombre as Proveedor

from StockMateriaPrima as stk inner join MateriaPrima as m on stk.idMateriaPrima = m.id
							  inner join Compra as com on com.id=stk.idOrdenCompra
                              inner join CompraStockMateria as comStk on comStk.idMateriaPrima = m.id
                              inner join Proveedor as p on com.idProveedor = p.id);

-- INSERCION DATOS--

USE renegade;

-- INSERCIONES DE ROL--
INSERT INTO Rol(name, description) VALUES ('cliente', 'Rol designado para los usuarios finales'),
                                          ('administrador', 'Rol designado para los administradores del sistema'),
                                          ('administrativo', 'Rol designado para los administrativos del sistema');

-- INSERCIONES USUARIO--
-- Las contrasenias son password --
INSERT INTO usuario(nombres, apellidos, correo, password, active, idRol) VALUES
('Nombre de administrador', 'Apellidos', 'administrador@gmail.com', 'sha256$1Ftzf32tZ0QCcdHj$0ebc4d9c6e18261e08f17a5fbc5572d7d6f3a75ea692dee2d59e2c1e2dbdb197', 1, 2),
('Nombre de administrativo', 'Apellidos', 'administrativo@gmail.com', 'sha256$1Ftzf32tZ0QCcdHj$0ebc4d9c6e18261e08f17a5fbc5572d7d6f3a75ea692dee2d59e2c1e2dbdb197', 1, 3),
('Nombre de cliente', 'Apellidos', 'cliente@gmail.com', 'sha256$1Ftzf32tZ0QCcdHj$0ebc4d9c6e18261e08f17a5fbc5572d7d6f3a75ea692dee2d59e2c1e2dbdb197', 1, 1);


-- INSERCIONES PROVEEDOR --
INSERT INTO proveedor (nombre, contacto, telefono, correo) VALUES
('Samper', 'Ricardo Flores', '477-487-00-10','ricardo-sanpersanper@samper.com'),
('Revilla', 'Juan Bosco', '477-785-87-00','revilla-bosco@outlook.com'),
('Modatelas', 'Cesar Romario', '477-123-00-70','modatelas-cesar@gmail.com'),
('Optimo', 'Juan Pascal', '477-855-04-07','juan-pascal@optimo.com');

-- INSERCIONES COMPRA --
INSERT INTO compra (folio,idProveedor, fechaCompra) VALUES
('f7a64a95-af4e-4590-a9d4-6d671418e07c', 1,'2022/03/30'),
('bb9c7ae0-8337-4b55-ba5d-94e35d17d775', 2,'2022/04/1'),
('921267b5-2844-452e-9fb6-fd19da9948f6', 3,'2022/04/1'),
('061de155-b634-4aff-bd6f-b28b4340670e', 4,'2022/04/2');

-- INSERSCIONES CATALOGO MATERIA PRIMA --
INSERT INTO MateriaPrima (nombre, descripcion, cantidad, unidad) VALUES
('Rollo de tela negra', 'Tela para el diseño de playeras', 50, 'metros'),
('Rollo de tela blanca', 'Tela para el diseño de playeras', 50, 'metros'),
('Rollo de hilo negro', 'Hilo para coser', 10, 'metros'),
('Paquete de etiquetas Renegade', 'Etiquetas para ropa', 100, 'unidad'),
('Bolsa de botones', 'Botones para ropa', 250 , 'unidades'),
('Paquete de resortes', 'Resortes multiusos', 100, 'unidades'),
('Paquete de cremalleras', 'Botones para ropa', 50 , 'unidades');

-- INSERCIONES STOCKCOMPRA --
INSERT INTO CompraStockMateria (idOrdenCompra, idMateriaPrima, Cantidad, costo) VALUES
(1, 1, 2, 1250), (1, 2, 2, 1250),
(2, 3, 2, 500),
(3, 4, 5, 750),
(4, 5, 1, 350), (4, 6, 2, 500);

-- INSERCIONES STOCKMATERIA --
INSERT INTO StockMateriaPrima (cantidad, idMateriaPrima, idOrdenCompra) VALUES
(100,1,1), (100,2,1),
(20,3,2),
(500,4,3),
(100,5,4), (100,6,4);


-- INSERCIONES PRODUCTO --
INSERT INTO renegade.producto(nombre, descripcion, precio, talla, image_url, activo) VALUES
('Playera lisa', 'Playera de cuello de redondo perfecta para salidades casuales', 0, 'Unitalla', 'https://optimabasicos.com/wp-content/uploads/2019/06/35464-00109.jpg', 1),
('Camiseta de tirantes', 'La primavera ya comenzó, con esta camiseta podrás pasar las tardes sin tanto calor', 0, 'Unitalla', 'https://www.ecamisetas.com/articulos/gr/camisetas-para-hombre-6545.jpg', 1),
('Pants sport', '¿Listo para descanar el fin de semana? Checa este pants, super cómodo', 0, 'Unitalla', 'https://img.joomcdn.net/5d49eb3480653a1a1b8cd3b788510a52100bbf84_original.jpeg', 1),
('Falda básica', 'Práctica y super cómoda falda !', 0, 'Unitalla', 'https://static.mujerhoy.com/www/multimedia/202006/13/media/cortadas/falda-mini-negra-zara-kKeG--600x900@MujerHoy.jpg', 1),
('Chaleco de vestir', 'Un chaleco sencillo y elegante', 0, 'Unitalla', 'https://ss246.liverpool.com.mx/xl/1074032512.jpg', 1),
('Calcentines de vestir', '¿Un evento importante? No olvides tus calcetines', 0, 'Unitalla', 'https://www.dim.com/dw/image/v2/AARR_PRD/on/demandware.static/-/Sites-dim-master/default/dw3a1ea463/DIM_05QV_0HZ_01.jpg?sw=600&sh=600&sm=fit', 1),
('Shorts sport', 'Shorts perfectos para ejercitarte', 0, 'Unitalla', 'https://www.iciw.com/bilder/artiklar/liten/11935-001_S.jpg?m=1643615888', 1),
('Vestido casual', 'Presume tu figura con nuestro diseño exclusico Renegade', 0, 'Unitalla', 'https://http2.mlstatic.com/D_NQ_NP_845013-MLM43775222401_102020-O.jpg', 1),
('Sudadera casual', '¿Un poco de frío? Checa esta sudadera genial', 0, 'Unitalla', 'https://cdn.shopify.com/s/files/1/0047/9163/1961/products/sudadera-blanca-para-sublimar-con-cangurera-y-capucha-D_NQ_NP_679100-MLM40194407561_122019-F_530x@2x.jpg?v=1600902284', 1),
('Bufanda', 'Protegete del invierno con nuestro diseño exclusivo', 0, 'Unitalla', 'https://www.regalopublicidad.com/images/rmlsw/458c6a74432200aea729c076e1c5/610-460/bufanda-de-poliester-para-el-frio.jpg', 1);

-- INSERCIONES Estructura --
-- TODO Faltan botones, hilos, etc...
INSERT INTO estructura(idProducto, idMateriaPrima, cantidad, descripcion) VALUES
(1, 2, 1, 'Vista frontal'), (1, 2, 1, 'Vista trasera'), (1, 2, 0.25, 'Mangas'),
(2, 2, 1, 'Vista frontal'), (2, 2, 1, 'Vista trasera'),
(3, 2, 0.5, 'Vista frontal'), (3, 2, 0.5, 'Vista trasera'),
(4, 2, 0.5, 'Pieza completa'),
(5, 1, 1, 'Vista trasera'), (5, 1, 0.5, 'Vista lateral derecha'), (5, 1, 0.5, 'Vista lateral izquierda'),
(6, 1, 0.25, 'Vista superior izquierda'), (6, 1, 0.25, 'Vista inferior izquierda '), (6, 1, 0.25, 'Vista inferior derecha'), (6, 1, 0.25, 'Vista superior derecha'),
(7, 2, 0.5, 'Vista frontal'), (7, 2, 0.5, 'Vista trasera'),
(8, 2, 1, 'Vista frontal'), (8, 2, 1, 'Vista trasera'),
(9, 2, 1, 'Vista frontal'), (9, 2, 1, 'Vista trasera'), (9,2,.5, 'Gorro'),
(10, 1, .75, 'Pieza completa');

-- INSERCIONES MaterialUsado --
#TODO Ayuda bebes, no se que datos van aqui.
INSERT INTO materialusado(idProducto, idStockMateriaPrima, cantidad) VALUES
(1,1,1);

-- INSERCIONES Carrito --
INSERT INTO carrito(status, idUsuario) VALUES
(0,3), (0,3), (1,3);

-- INSERCIONES productocarrito --
#TODO Precio incorrecto
INSERT INTO productocarrito(idProducto, idCarrito, cantidad, precio) VALUES
(1, 1, 2, 250), (5, 1, 1, 100), (8, 1, 1, 200),
(1, 2, 2, 250),
(1, 3, 3, 250), (5, 3, 3, 100), (8, 3, 3, 200), (4,3,1,600);

INSERT INTO  venta(folio, total, fecha, idCarrito) VALUES
('1282d0c2-74ed-4a08-a1a0-df2179a63564', 550, '2022/03/29', 1),
('feddb073-197d-441e-bc34-a423a96656a2', 250, '2022/03/30', 2);