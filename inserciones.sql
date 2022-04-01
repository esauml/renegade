-- INSERCIONES PROVEEDOR --
insert into proveedor (nombre, contacto, telefono, correo)
values ('proveedorTela', 'agenteProveedorTela', '477-000-00-00','correo@proveedor'),
    ('proveedorTela2', 'agenteProveedorTela2', '477-000-00-00','correo1@proveedor'),
    ('proveedorTela3', 'agenteProveedorTela3', '477-000-00-00','correo2@proveedor'),
    ('proveedorTela4', 'agenteProveedorTela4', '477-000-00-00','correo3@proveedor');

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

-- INSERCIONES DE ROL--
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


Insert Into producto(nombre, descripcion, precio, talla, stock, image_url)
VALUES ('Playera', 'Playera', 10, 'Unitalla', 0, ''),
       ('Camiseta', 'Camiseta', 20, 'Unitalla', 0, ''),
       ('Pants', 'Pants', 30, 'Unitalla', 0, ''),
       ('Falda', 'Falda', 40, 'Unitalla', 0, ''),
       ('Chaleco', 'Chaleco', 50, 'Unitalla', 0, ''),
       ('Calcetines', 'Calcetines', 60, 'Unitalla', 0, ''),
       ('Shorts', 'Shorts', 70, 'Unitalla', 0, ''),
       ('Vestido', 'Vestido', 80, 'Unitalla', 0, ''),
       ('Sudadera', 'Sudadera', 90, 'Unitalla', 0, ''),
       ('Bufandas', 'Bufandas', 100, 'Unitalla', 0, '');


