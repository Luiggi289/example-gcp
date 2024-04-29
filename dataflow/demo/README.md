
## DataFlow


gcloud services enable dataflow.googleapis.com


#### Copiar el repositorio 
```
cd
rm -r example-gcp -f
git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/dataflow/demo
```


pip install wheel

pip3 install apache-beam[gcp]

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