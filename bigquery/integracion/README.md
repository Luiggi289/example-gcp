### Bigquery




### Cargar datos con comandos BQ


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



### Cargar tablas con SQL
####  (cambiar premium-guide-410714 por el id de tu proyecto)

#### Crear conjunto de datos 

CREATE SCHEMA `premium-guide-410714.dm_sale` 

  OPTIONS (    location = 'US'); 



#### Crear Tabla 


create or replace table  `premium-guide-410714.dm_sale.bi_sale`
(
date DATE,
category_name STRING,
city STRING ,
county STRING ,
city_type STRING ,
vendor_name STRING,
sales_dollars FLOAT64 
) 
PARTITION BY date
CLUSTER BY city_type
OPTIONS (
  description = "tabla bi de ventas",
  partition_expiration_days = 1095 ## fecha con mas de 3 años de antiguedad se borran
);


#### Cargar Tabla con dos cluster
TRUNCATE TABLE  `premium-guide-410714.dm_sale.bi_sale` ;

INSERT INTO `premium-guide-410714.dm_sale.bi_sale`
(
date ,
category_name ,
city  ,
county  ,
vendor_name,
city_type  ,
sales_dollars  

)

SELECT date ,
category_name ,
city  ,
county  ,
vendor_name,
'A' city_type  , 
sum(sale_dollars) sale_dollars
FROM `bigquery-public-data.iowa_liquor_sales.sales` 
WHERE SUBSTRING (city,1,1) IN ('A','B','C','D','E','F','G','H')
group by 1,2 ,3,4,5
;




INSERT INTO `premium-guide-410714.dm_sale.bi_sale`
(
date ,
category_name ,
city  ,
county  ,
vendor_name,
city_type  ,
sales_dollars  

)


SELECT date ,
category_name ,
city  ,
county  ,
vendor_name,
'B' city_type  , 
sum(sale_dollars) sale_dollars
FROM `bigquery-public-data.iowa_liquor_sales.sales` 
WHERE SUBSTRING (city,1,1) NOT IN ('A','B','C','D','E','F','G','H')
group by 1,2 ,3,4,5;


