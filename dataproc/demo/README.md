
### Dataproc



git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/dataproc/demo

#### Ejecutar el comando :

gcloud services enable dataproc.googleapis.com

#### Creamos un Bucket en Cloud Storage

gsutil mb -l us-central1 gs://$DEVSHELL_PROJECT_ID-dataproc

#### Subir el archivo dataproc_init.sh a Cloud Storage

gcloud storage cp dataproc_init.sh gs://$DEVSHELL_PROJECT_ID-dataproc


#### Crear dataproc 
gcloud dataproc clusters create cluster01 --region=us-central1 \
--zone=us-central1-f \
--single-node \
--master-machine-type=n1-standard-2 \
--initialization-actions gs://$DEVSHELL_PROJECT_ID-dataproc/dataproc_init.sh

#### Avanzar despues de creado el cluster

