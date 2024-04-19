### Procedimiento para desplegar 

##### Ejecutar los siguientes comandos 

git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/memorystore/demo

#### Habilitar la Api de Memory store con Redis

gcloud services enable redis.googleapis.com


### 1 Crear una instancia de Redis 

#### 1.1 Ejecutar el siguiente comando 


gcloud redis instances create mem-redis-1 --size=2 --region=us-central1 --tier=basic --redis-config=notify-keyspace-events=gxE


--size=2 especifica el tamaño de la instancia en GB. En este caso, la capacidad de 2GB.
--region=us-central1 indica la región en la que deseas desplegar la instancia. Puedes cambiar us-central1 por la región que desees.
--tier=basic define el nivel de servicio de la instancia. En este caso, se utiliza el nivel básico.
--redis-config=notify-keyspace-events=gxE es opcional y puede ser necesario dependiendo de los requisitos de tu aplicación. Este parámetro habilita la notificación de eventos de espacio de claves.

### 1.2 Eliminar instancia
gcloud redis instances delete mem-redis-1 --region=us-central1