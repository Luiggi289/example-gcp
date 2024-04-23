### Procedimiento para desplegar 

##### Ejecutar los siguientes comandos 

git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/bigquery/integracion


##### Ejecutar el siguiente comando :

gsutil cp data/master/product.csv gs://test-nh/data/master/product.csv

bq load --skip_leading_rows=1 \ ​
--field_delimiter=',' \
--source_format=CSV \ ​
premium-guide-410714.dep_raw.product \ ​
gs://test-nh/data/master/product.csv \ ​
'id:INTEGER,Product:STRING,prices_STRING,stock:STRING,color:STRING'