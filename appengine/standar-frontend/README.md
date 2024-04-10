
# 1- Abri una cloud shell de GCP

# 2- Ejecutar el siguiente comando reemplazando la variable PROJECT_ID:

gcloud config set project [PROJECT_ID]

# 3- Clonar el repositorio 

git clone https://github.com/Luiggi289/example-gcp.git 

# 4.- Abrir el archivo app.yaml y cambiar el valor de la variable de entorno SERVER_URL  , 
# El valor que debe ir debe ser el url del servicio front end de la aplicación

# 5.-Ejecutar el siguiente comando

cd example-gcp/function

# 6.- Ejecutar el siguiente comando reemplazando la variable:

gcloud app deploy



