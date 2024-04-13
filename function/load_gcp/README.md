## Procedimiento para el despliegue

### Ejecutar el siguiente comando reemplazando el valor de la variable PROJECT_ID

gcloud config set project [PROJECT_ID]

### Ejecutar el siguiente comando para clonar el proyecto  que está en github 

git clone https://github.com/Luiggi289/example-gcp.git 
cd example-gcp/function/load_gcp

### Ejectar el siguiente comando para desplegar el codigo a Cloud Function

gcloud functions deploy prd-load_tipo_cambio \
--gen2 \
--runtime=python312 \
--region=us-central1 \
--source=. \
--entry-point=load_tipo_cambio \
--trigger-http \
--no-allow-unauthenticated

### Ejecutar el siguiente comando para ejecutar la cloud function para cargar a Cloud storage 
### Antes cambiar la variable target

curl -m 70 -X POST https://us-central1-premium-guide-410714.cloudfunctions.net/prd-load_tipo_cambio \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{
  "load_type": "storage",
 "target":"gs://test-nh/tipo_cambio.csv"
}'


### Ejecutar el siguiente comando para ejecutar la cloud function para cargar a Bigquery 
### Antes cambiar la variable target

curl -m 70 -X POST https://us-central1-premium-guide-410714.cloudfunctions.net/prd-load_tipo_cambio \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{
  "load_type": "bigquery",
 "target":"premium-guide-410714.dep_raw.exchange_rate_v2"
}'
    