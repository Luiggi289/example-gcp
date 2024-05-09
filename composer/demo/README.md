
## Cloud Composer

### Ir a cloud Shell y Copiar el repositorio  ejecutando el siguiente comando : 
```
cd
rm -r example-gcp -f
git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/composer/demo
```
copiar el archivo requirements

gcloud iam service-accounts create prd-orquestador-data-airflow

gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID \
  --member="serviceAccount:prd-orquestador-data-airflow@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/bigquery.jobUser"

Dar acceso a dataset
acceso de Administrador de alamacenamiento 

crear la conexion en astronomer

dar acceso de cloud function invoker
astro-quasarian-spectrum-7268@astro-us-central1-0001.iam.gserviceaccount.com

