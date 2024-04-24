
### Bigtable

git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/bigtable/demo

#### Creamos una tabla en bitable :

cbt -project premium-guide-410714 -instance bigtable-inst createtable clientes

#### Creamos las familias de columna :

cbt -project premium-guide-410714 -instance bigtable-inst createfamily clientes datos_cliente
cbt -project premium-guide-410714 -instance bigtable-inst createfamily clientes datos_adicionales

### Cargar  datos de prueba ejecutado el siguiente comando :

python main.py

#### Ejecutar la siguiente consulta para crear una tabla particinada

CREATE EXTERNAL TABLE premium-guide-410714.dep_raw.test_bigtable
OPTIONS (
  format = 'CLOUD_BIGTABLE',
  uris = ['https://googleapis.com/bigtable/projects/premium-guide-410714/instances/bigtable-inst/tables/test'],
  bigtable_options =
    """
    {
      columnFamilies: [
        {
          "familyId": "cf1",
          "type": "STRING",
          "encoding": "BINARY"
        },
        {
          "familyId": "cf2",
          "type": "STRING",
          "encoding": "BINARY"
        }
      ],
      readRowkeyAsString: true
    }
    """
);