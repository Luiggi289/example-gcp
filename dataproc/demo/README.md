
## Dataproc

### 1. Mi primer programa en Dataproc

#### Copiar el repositorio 
```
cd
rm -r example-gcp -f
git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/dataproc/demo
```

#### Ejecutar el comando :
```
gcloud services enable dataproc.googleapis.com
```

#### Creamos un Bucket en Cloud Storage
```
gcloud storage buckets create gs://$DEVSHELL_PROJECT_ID-dataproc-dev --location=us-central1
```
#### Subir el archivo dataproc_init.sh a Cloud Storage
```
gsutil cp dataproc_init.sh gs://$DEVSHELL_PROJECT_ID-dataproc-dev
```

#### Crear dataproc 
```
gcloud dataproc clusters create cluster01 --region=us-central1 \
--zone=us-central1-f \
--single-node \
--master-machine-type=n1-standard-2 \
--initialization-actions gs://$DEVSHELL_PROJECT_ID-dataproc-dev/dataproc_init.sh
```




#### Avanzar despues de creado el cluster

#### Copiar el archivo con el codigo a ejecutar
```
gsutil cp main.py gs://$DEVSHELL_PROJECT_ID-dataproc-dev
```

#### Crear un Job y ejecutarlo

```
gcloud dataproc jobs submit pyspark \
gs://$DEVSHELL_PROJECT_ID-dataproc-dev/main.py \
--cluster=cluster01 \
--region=us-central1 
```


### 2. Integración con Bigquery


#### Crear el dataset donde se van a crear mi tabla destino
```

CREATE SCHEMA IF NOT EXISTS `premium-guide-410714.datamart_ventas` 
  OPTIONS (    location = 'US'); 

```

#### Crear la siguiente tabla que será la fuente para el proceso en spark
```

create or replace table premium-guide-410714.datamart_ventas.input_segmentacion as
select a.user_id ,  cast(a.created_at as date) order_date,sum(b.sale_price) sale_price  from 
bigquery-public-data.thelook_ecommerce.orders a
inner join bigquery-public-data.thelook_ecommerce.order_items b 
on a.order_id=b.order_id
where a.status='Complete'
group by 1,2

```
#### Crear Storge temporal que usará Dataproc
```
gcloud storage buckets create gs://$DEVSHELL_PROJECT_ID-dataproc-tmp --location=us-central1
```
#### Copiar en un bucket mi codigo 
```
gsutil cp segment.py gs://$DEVSHELL_PROJECT_ID-dataproc-dev
```

#### Validar versión de SPARK en el cluster

https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.0

#### validar versiones compatibles del conector bigquery con Spark

https://github.com/GoogleCloudDataproc/spark-bigquery-connector?tab=readme-ov-file

#### descargar el conector  de bigquery con Spark 

```
curl -o spark-3.1-bigquery-0.37.0.jar https://storage.googleapis.com/spark-lib/bigquery/spark-3.1-bigquery-0.37.0.jar
```

#### Subir el conector de Bigquery a un Bucket
```
gsutil cp spark-3.1-bigquery-0.37.0.jar gs://$DEVSHELL_PROJECT_ID-dataproc-dev/spark-3.1-bigquery-0.37.0.jar
```

#### Ejecutar un job de Dataproc , aquí se ejecuta mi código python 
```
gcloud dataproc jobs submit pyspark \
gs://$DEVSHELL_PROJECT_ID-dataproc-dev/segment.py \
--cluster=cluster01 \
--region=us-central1 \
--jars=gs://$DEVSHELL_PROJECT_ID-dataproc-dev/spark-3.1-bigquery-0.37.0.jar
```


#### Eliminar el cluster
```
gcloud dataproc clusters delete cluster01 --region=us-central1
```







