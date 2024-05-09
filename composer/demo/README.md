
## Cloud Composer

### Ir a cloud Shell y Copiar el repositorio  ejecutando el siguiente comando : 
```
cd
rm -r example-gcp -f
git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/composer/demo
```

### copiar el archivo requirements.txt en su repositorio personal

### crear una cuenta de servicio 
```
gcloud iam service-accounts create prd-orquestador-data-airflow
```
### Dar acceso de Job User a la cuenta de servicio creada
```
gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID \
  --member="serviceAccount:prd-orquestador-data-airflow@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/bigquery.jobUser"
```

#### Dar acceso de editor a la cuenta de servicio creada  al dataset raw_ventas 
#### acceso de Administrador de alamacenamiento al bucket donde se guardará el archivo de tipo_cambio.csv

#### crear la conexion en astronomer

#### dar acceso de cloud function invoker  a la cuenta creada 

