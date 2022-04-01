CREATE USER 'cliente'@'localhost' identified by '8+9Jw+3*2mE';
GRANT SELECT,UPDATE ON renegade.usuario TO 'cliente'@'localhost';
GRANT SELECT,INSERT ON renegade.carrito TO 'cliente'@'localhost';
GRANT SELECT,INSERT,UPDATE ON renegade.productocarrito TO 'cliente'@'localhost';
GRANT SELECT,INSERT ON renegade.venta TO 'cliente'@'localhost';

CREATE USER "administrativo"@"localhost" IDENTIFIED BY "X0u^HTVGt";
GRANT SELECT ON renegade.usuario TO "administrativo"@"localhost";
GRANT SELECT ON renegade.compra TO "administrativo"@"localhost";
GRANT SELECT ON renegade.comprastockmateria TO "administrativo"@"localhost";
GRANT SELECT ON renegade.estructura TO "administrativo"@"localhost";
GRANT SELECT ON renegade.materialusado TO "administrativo"@"localhost";
GRANT SELECT ON renegade.materiaprima TO "administrativo"@"localhost";
GRANT SELECT ON renegade.pedido TO "administrativo"@"localhost";
GRANT SELECT ON renegade.producto TO "administrativo"@"localhost";
GRANT SELECT ON renegade.productocarrito TO "administrativo"@"localhost";
GRANT SELECT ON renegade.proveedor TO "administrativo"@"localhost";
GRANT SELECT ON renegade.stockmateriaprima TO "administrativo"@"localhost";

CREATE USER "administrador"@"localhost" IDENTIFIED BY "|C226gmlnbm";
GRANT SELECT,INSERT, UPDATE ON renegade.usuario TO "administrador"@"localhost";
GRANT SELECT,INSERT, UPDATE ON renegade.compra TO "administrador"@"localhost";
GRANT SELECT,INSERT, UPDATE ON renegade.comprastockmateria TO "administrador"@"localhost";
GRANT SELECT,INSERT, UPDATE ON renegade.estructura TO "administrador"@"localhost";
GRANT SELECT,INSERT, UPDATE ON renegade.materialusado TO "administrador"@"localhost";
GRANT SELECT,INSERT, UPDATE ON renegade.materiaprima TO "administrador"@"localhost";
GRANT SELECT,INSERT, UPDATE ON renegade.pedido TO "administrador"@"localhost";
GRANT SELECT,INSERT, UPDATE ON renegade.producto TO "administrador"@"localhost";
GRANT SELECT,INSERT, UPDATE ON renegade.productocarrito TO "administrador"@"localhost";
GRANT SELECT,INSERT, UPDATE ON renegade.proveedor TO "administrador"@"localhost";
GRANT SELECT,INSERT, UPDATE ON renegade.rol TO "administrador"@"localhost";

FLUSH PRIVILEGES;

SHOW GRANTS FOR "administrador"@"localhost";
SHOW GRANTS FOR "administrativo"@"localhost";
SHOW GRANTS FOR "cliente"@"localhost";