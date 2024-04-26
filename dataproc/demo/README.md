
### Dataproc


#### Copiar el repositorio 
git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/dataproc/demo

#### Ejecutar el comando :

gcloud services enable dataproc.googleapis.com

#### Creamos un Bucket en Cloud Storage

gcloud storage buckets create gs://$DEVSHELL_PROJECT_ID-dataproc-dev --location=us-central1

#### Subir el archivo dataproc_init.sh a Cloud Storage

gsutil cp dataproc_init.sh gs://$DEVSHELL_PROJECT_ID-dataproc-dev


#### Crear dataproc 
gcloud dataproc clusters create cluster01 --region=us-central1 \
--zone=us-central1-f \
--single-node \
--master-machine-type=n1-standard-2 \
--initialization-actions gs://$DEVSHELL_PROJECT_ID-dataproc-dev/dataproc_init.sh

#### Avanzar despues de creado el cluster

gcloud storage cp main.py gs://$DEVSHELL_PROJECT_ID-dataproc-dev

#### Crear un Job y ejecutarlo

gcloud dataproc jobs submit pyspark \
gs://$DEVSHELL_PROJECT_ID-dataproc-dev/main.py \
--cluster=cluster01 \
--region=us-central1 





CREATE SCHEMA IF NOT EXISTS `premium-guide-410714.datamart_ventas` 
  OPTIONS (    location = 'US'); 


    
gcloud storage buckets create gs://$DEVSHELL_PROJECT_ID-dataproc-dev --location=us-central1


