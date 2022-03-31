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
                              inner join Proveedor as p on com.idProveedor = p.id
);
