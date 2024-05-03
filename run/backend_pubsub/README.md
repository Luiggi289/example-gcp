

#### Copiar el repositorio 
```
cd
rm -r example-gcp -f
git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/run/backend_pubsub
```

#### Crear Imagen Docker
```
 gcloud builds submit --tag gcr.io/$DEVSHELL_PROJECT_ID/backendcard 
```

#### Desplegar Cloud Run
```
gcloud run deploy service-card --image gcr.io/$DEVSHELL_PROJECT_ID/backendcard  \
--platform managed \
--region us-central1 \
--allow-unauthenticated \
--max-instances 2 \
--memory 4Gi 
```


