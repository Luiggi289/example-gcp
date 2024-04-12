### Procedimiento para desplegar 

##### Ejecutar los siguientes comandos 

git clone https://github.com/Luiggi289/example-gcp.git  <br />
cd example-gcp/storage/gsutil

##### Ejecutar el siguiente comando para windows:

.\load_storage.ps1

##### Ejecutar el siguiente comando para linux:

sh load_storage.sh

#### Ejecutar procesos con cuenta de servicio

##### Crear cuenta de servicio con el siguiente comando

gcloud iam service-accounts create prd-process-data-onpremise

##### 

gcloud iam service-accounts keys create prd-process-data-onpremise.json --iam-account=prd-process-data-onpremise@premium-guide-410714.iam.gserviceaccount.com

