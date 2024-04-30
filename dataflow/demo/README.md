
### DataFlow


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


### Plantillas de Dataflow 

#### Revisa la documentación en : 
```
https://cloud.google.com/dataflow/docs/guides/templates/provided-templates
```


### Cargar datos desde Firestore a Cloud Storage

```
gcloud dataflow jobs run job-ingesta-firestore \
    --gcs-location gs://dataflow-templates-southamerica-west1/latest/Firestore_to_GCS_Text \
    --region southamerica-west1 \
    --parameters \
firestoreReadGqlQuery="SELECT * FROM transacciones",\
firestoreReadProjectId=premium-guide-410714,\
textWritePrefix=gs://premium-guide-410714-dataflow-dev/firestore/transacciones
--num-workers=1
```