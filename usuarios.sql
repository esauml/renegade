GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
-- SHOW GRANTS FOR "root"@"localhost";
FLUSH PRIVILEGES;

-- Cliente
DROP USER IF EXISTS 'cliente'@'localhost';
CREATE USER 'cliente'@'localhost' identified by '8+9Jw+3*2mE';
GRANT SELECT, INSERT, UPDATE ON renegade.usuario TO 'cliente'@'localhost';
GRANT SELECT, INSERT ON renegade.carrito TO 'cliente'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON renegade.productocarrito TO 'cliente'@'localhost';
FLUSH PRIVILEGES;

-- Administrativo
-- # TODO Usuario quitar vista pra administrativo, lo controla el adm
DROP USER IF EXISTS 'administrativo'@'localhost';
CREATE USER 'administrativo'@'localhost' IDENTIFIED BY 'X0u^HTVGt';
GRANT SELECT, INSERT, UPDATE ON renegade.comprastockmateria TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.compra TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.estructura TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.materialusado TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.materiaprima TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.pedido TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.producto TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.productocarrito TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.proveedor TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.rol TO "administrador"@"localhost";
GRANT SELECT ON renegade.venta TO "administrador"@"localhost";


-- ADMINISTRADOR
DROP USER IF EXISTS 'admnistrador'@'localhost';
CREATE USER 'admnistrador'@'localhost' IDENTIFIED BY 'X0u^HTVGt';
GRANT SELECT, INSERT, UPDATE ON renegade.usuario TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.compra TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.comprastockmateria TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.estructura TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.materialusado TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.materiaprima TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.pedido TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.producto TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.productocarrito TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.proveedor TO "administrador"@"localhost";
GRANT SELECT, INSERT, UPDATE ON renegade.rol TO "administrador"@"localhost";
FLUSH PRIVILEGES;

SHOW GRANTS FOR "administrador"@"localhost";
SHOW GRANTS FOR "administrativo"@"localhost";
SHOW GRANTS FOR "cliente"@"localhost";

