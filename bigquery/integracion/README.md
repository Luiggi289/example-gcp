### Procedimiento para desplegar 

##### Ejecutar los siguientes comandos 

git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/bigquery/integracion


##### Ejecutar el siguiente comando para subir un archivo a GCS:

gsutil cp data/master/product.csv gs://test-nh/data/master/product.csv

##### Ejecutar el siguiente comando para cargar una tabla con un archivo de GCS:
bq load --skip_leading_rows=1 \
--field_delimiter=',' \
--source_format=CSV \
dep_raw.product \
gs://test-nh/data/master/product.csv \
'id:INTEGER,Product:STRING,prices:STRING,stock:STRING,color:STRING'