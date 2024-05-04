
### 1.- Intudcción DataFlow


#### Abrir Cloud Shell

```
gcloud services enable dataflow.googleapis.com
```


#### Copiar el repositorio 
```
cd
rm -r example-gcp -f
git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/dataflow/demo
```

### Instalar la biblioteca wheel
```
pip install wheel
```
### Instalar la biblioteca Apache Beam para GCP

```
pip3 install apache-beam[gcp]
```

#### Creamos un Bucket en Cloud Storage para los metadatos de Dataflow
```
gcloud storage buckets create gs://$DEVSHELL_PROJECT_ID-dataflow-dev --location=us-central1
```


#### Creamos un Bucket en Cloud Storage para los temporales de Dataflow
```
gcloud storage buckets create gs://$DEVSHELL_PROJECT_ID-dataflow-tmp-dev --location=us-central1
```

#### Creamos un Bucket en Cloud Storage para nuestro datalake
```
gcloud storage buckets create gs://$DEVSHELL_PROJECT_ID-datalake-dev --location=us-central1
```


#### Ejecutamos el código python para hacer el despliegue 


python demo.py


### 2.- Plantillas de Dataflow 

#### Revisa la documentación en : 
```
https://cloud.google.com/dataflow/docs/guides/templates/provided-templates
```


### Cargar datos desde Firestore a Cloud Storage en Lote

#### Ingesamos a Cloud Shell :
```
https://shell.cloud.google.com/
```

#### Ejecutar el siguiente comando :

```
gcloud dataflow jobs run job-ingesta-firestore \
    --gcs-location gs://dataflow-templates-southamerica-west1/latest/Firestore_to_GCS_Text \
    --region southamerica-west1 \
    --parameters \
firestoreReadGqlQuery="SELECT * FROM transacciones",\
firestoreReadProjectId=$DEVSHELL_PROJECT_ID,\
textWritePrefix=gs://$DEVSHELL_PROJECT_ID-datalake-dev/firestore/transacciones \
--num-workers=1
```


#### 3.- Cargar datos a bigquery en Streaming

### Creamos un Tema(tópico) con el siguiente comando

```
gcloud pubsub topics create topic_card
```

### Ir a Bigquery Estudio y ejecutar el siguiente Script para crear el esquema 
```
CREATE SCHEMA IF NOT EXISTS `datamart_ventas`  

  OPTIONS (    location = 'US'); 
```

####  3.1 Cargar datos a bigquery con Dataflow (Opcional)


### Creamos una suscripción con el siguiente comando
```
gcloud pubsub subscriptions create subs_card --topic=topic_card
```

###  Creamos la tabla donde se guardarón los siguiente registros 
### Entramos a Bigquery Studio y ejecutamos la siguiente sentencia : 
```
create or replace table  datamart_ventas.stream_tarjeta_dfw
(

name string,
email string ,
document string ,
comments string,
card string ,
created_datetime string 


)
```



### Crear un Job Stream en dataflow 

### Documentación 
```
https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-bigquery
```

### Creamos el job streaming en dataflow con los siguientes pasos :

####	1.- Ir a la consola de GCP , ir al menú de navegación y seleccionar el producto Dataflow
####	2.- Ir al sección "trabajos" y dar clic al botón  "CREAR TRABAJO A PARTIR DE UNA PLANTILLA".
####	3.- En el campo Nombre del trabajo, ingrese un nombre de trabajo único : job-stream-bq.
####	4.- para Punto final regional, seleccione un valor en el menú desplegable. La región predeterminada es us-central1.
####	5.- En el menú desplegable Plantilla de flujo de datos, seleccione la plantilla Pub/Sub Subscription to BigQuery.
####	6.- En el campo "Bigquery ouput table" ingresar el nombre de su tabla , para este ejercicio usaremos  premium-guide-410714.datamart_ventas.stream_tarjeta_dfw
####	7.- En la lista desplegable "Pub/Sub input subscription" seleccionamos una suscripción , para este ejercicio usaremos "subs_card"
#### 8.- En el campo Ubicación Temporal ingresamos el valor : 
```
PROJECT_ID-dataflow-tmp-dev/tmp
```
#### 9.- En el campo "Máx. de Trabajadores" , ingresar el valor 1
#### 10.- Finalmente clic en "Ejecutar Trabajo"




#### Probar el proceso en Streaming

#### Ir a Cloud Shell
#### Copiar el repositorio 
```
cd
rm -r example-gcp -f
git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/dataflow/demo
```

#### Crear un entorno virtual  
```
virtualenv env
```
#### Activar el entorno Virtual
```
source env/bin/activate
```
#### Instalar las librerias 
```
pip install -r requirements.txt
```
#### Ejecutar Código python donde se hace la publicacón de mensajes :
```
python pubsub_publish.py
```


### 3.3 Cancelar el Job de Dataflow
#### Para evitar costos por el job tipo Streaming , debemos cancelar el Job 
#### 1.- Ir a Dataflow en la sección de trabajos
#### 2.- Seleccionar el job en ejecución :  job-stream-bq 
#### 3.- Dar clic en el botón "DETENER"


### 3.2.- Cargar Datos a Bigquery solo con Pubsub


#### Primero crearemos una tabla donde se almacenarán los mensajes de pubsub
#### Ir a Bigquery Estudio y ejecutar el siguiente Script para crear la tabla 
```
CREATE TABLE
  datamart_ventas.venta_online (
subscription_name STRING,
message_id STRING,
publish_time TIMESTAMP,
data JSON,
attributes STRING ,
  )
PARTITION BY DATE(publish_time)
OPTIONS(
  partition_expiration_days=90
);

```
#### Creamos una suscripción en Pubsub
#### 1.- Vamos a pubsub y seleccionamos la sección Suscripciones
#### 2.- Damos clic en el botón "CREAR SUSCRIPCIÓN"
#### 3.- En ID de la suscripción ingesamos : susc_venta_enlinea
#### 4.- Seleccionamos el tema topic-card
#### 5.- En Tipo de Envio Seleccionamos "Escribe en Bigquery"
#### 6.- Seleccionamos el proyecto de prueba y seleccionamos el esquema datamart_ventas
####     (En alguno es necesario dar permisos de editor a la cuenta de servicio que usa pub/sub)
#### 7.- Seleccionamos la tabla venta_online
#### 8.- En Schema Option Seleccionamos "Ninguno" y marcamos la opción "Escribir Metadatos"
#### 9.- Finalmente damos clic en el botón "CREAR"


#### Probemos ejecutando el siguiente código en cloud shell 
```
python pubsub_publish.py
```

#### creamos una vista que usaremos para hacer los reportes
```
CREATE OR REPLACE VIEW datamart_ventas.v_venta_online
as
SELECT
publish_time fecha,
1 tarjetas,
CASE   
      WHEN SUBSTR( STRING (JSON_EXTRACT(json_text, '$.card') ),0,1)='1' THEN 'VISA-DEBITO' 
      WHEN SUBSTR(STRING (JSON_EXTRACT(json_text, '$.card') ),0,1) ='2' THEN 'VISA-CREDITO' 
      WHEN SUBSTR(STRING (JSON_EXTRACT(json_text, '$.card') ),0,1) ='3' THEN 'MC-DEBITO' 
      WHEN SUBSTR(STRING (JSON_EXTRACT(json_text, '$.card') ),0,1) ='4' THEN 'MC-CREDITO' 
      WHEN SUBSTR(STRING (JSON_EXTRACT(json_text, '$.card') ),0,1) ='9' THEN 'MC-CREDITO' 
      ELSE 'VIRTUAL'

      END as tipo_tarjeta

 FROM  premium-guide-410714.datamart_ventas.venta_online  a
,UNNEST  ( [a.data ]) as json_text
;
```