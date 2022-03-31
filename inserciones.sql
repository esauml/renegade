
-- INSERCIONES PROVEEDOR --
insert into proveedor (nombre, contacto, telefono, correo)
values ('proveedorTela', 'agenteProveedorTela', '477-000-00-00','correo@proveedor');

-- INSERCIONES COMPRA --
insert into compra (folio,idProveedor, fechaCompra) 
values ('00001', 1,'2022/03/30');
insert into compra (folio,idProveedor, fechaCompra) 
values ('00002', 1,'2022/03/30');



-- INSERSCIONES CATALOGO MATERIA PRIMA --
insert into MateriaPrima (nombre, descripcion, cantidad, unidad)
values ('Rollo de tela negra', 'Tela para el diseño de playeras', 50, 'metros');
insert into MateriaPrima (nombre, descripcion, cantidad, unidad)
values ('Rollo de tela blanca', 'Tela para el diseño de playeras', 50, 'metros'); 



-- INSERCIONES STOCKCOMPRA --
insert into CompraStockMateria (idOrdenCompra, idMateriaPrima, Cantidad, costo)
values (1,1,1,250.00);
insert into CompraStockMateria (idOrdenCompra, idMateriaPrima, Cantidad, costo)
values (1,2,3,255.00);

-- INSERCIONES STOCKMATERIA -- 
insert into StockMateriaPrima (cantidad, idMateriaPrima, idOrdenCompra) values (50, 1,1);
INSERT INTO StockMateriaPrima (cantidad, idMateriaPrima, idOrdenCompra) values (50, 2,1);
INSERT INTO StockMateriaPrima (cantidad, idMateriaPrima, idOrdenCompra) values (50, 2,1);
INSERT INTO StockMateriaPrima (cantidad, idMateriaPrima, idOrdenCompra) values (50, 2,1);