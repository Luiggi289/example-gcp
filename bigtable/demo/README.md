
### Bigtable
####  (cambiar premium-guide-410714 por el id de tu proyecto)

git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/bigtable/demo

#### Creamos una tabla en bitable :

cbt -project premium-guide-410714 -instance bigtable-inst createtable clientes

#### Creamos las familias de columna :

cbt -project premium-guide-410714 -instance bigtable-inst createfamily clientes datos_cliente
cbt -project premium-guide-410714 -instance bigtable-inst createfamily clientes datos_adicionales

### Cargar  datos de prueba ejecutado el siguiente comando :

python main.py



#### Crear conjunto de datos 

CREATE SCHEMA `premium-guide-410714.dm_sale` 

  OPTIONS (    location = 'US'); 


#### Ejecutar la siguiente consulta para crear una tabla particinada


CREATE EXTERNAL TABLE premium-guide-410714.dm_sale.clientes
OPTIONS (
  format = 'CLOUD_BIGTABLE',
  uris = ['https://googleapis.com/bigtable/projects/premium-guide-410714/instances/bigtable-inst/tables/clientes'],
  bigtable_options =
    """
    {
      columnFamilies: [
        {
          "familyId": "datos_cliente",
          "type": "STRING",
          "encoding": "BINARY"
        },
        {
          "familyId": "datos_adicionales",
          "type": "STRING",
          "encoding": "BINARY"
        }
      ],
      readRowkeyAsString: true
    }
    """
);


#### Consultar tabla con UNNEST()

select rowkey,b.name ,c.value
 from `premium-guide-410714.dm_sale.clientes` a 
, UNNEST (datos_cliente.column) b
, UNNEST (b.cell) c
