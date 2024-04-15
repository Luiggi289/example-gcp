### Procedimiento para desplegar 

##### Ejecutar los siguientes comandos 

git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/storage/gsutil

##### Ejecutar el siguiente comando para windows:

.\load_storage.ps1

##### Ejecutar el siguiente comando para linux:

sh load_storage.sh

##### Documentación de comandos :
##### https://cloud.google.com/storage/docs/gsutil/commands/help

#### Ejecutar procesos con cuenta de servicio

##### Crear cuenta de servicio con el siguiente comando

gcloud iam service-accounts create prd-process-data-onpremise

##### Ejecutar el siguiente comando para generar una llave privada 
##### de la cuenta de servicio (antes cambiar el valor "premium-guide-410714" por
##### tu ID_PROJECT)

gcloud iam service-accounts keys create prd-process-data-onpremise.json \
--iam-account=prd-process-data-onpremise@premium-guide-410714.iam.gserviceaccount.com

##### Activar la autentificación por cuenta de servicio
gcloud auth activate-service-account --key-file=/home/moralesmeza28t/sensitive/prd-process-data-onpremise.json

##### Ver la lista de cuentas configurdas en el SDK de Google
gcloud auth list

##### Cambiar la autentificación en el SDK de Google
gcloud auth login

##### dara acceso de creador de objetos a una cuenta de servicio
gsutil iam ch serviceAccount:prd-process-data-onpremise@premium-guide-410714.iam.gserviceaccount.com:objectCreator gs://test-nh