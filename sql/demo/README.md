### Procedimiento para desplegar 


### 1 Crear una instancia SQL

##### 1.1. Ir al menú de navegación de cloud Console , en base de datos haga 
##### clic en  SQL

#### 1.2 Luego clic en el botón "CREAR INSTANCIA" o "CREAR INSTANCIA CON CRÉDITOS GRATUITOS"

#### 1.3 Elegir el motor de base de datos , para el presento ejercicio seleccionaremos Mysql
#### 1.4 Creamos la instancia , para el ejecicio usaremos el nombre test-bd-sql , luego creamos 
####     y guardamos la contraseña , finalmente seleccionamos la Edición Enterprise
#### 1.5 Elegimos la ubicación para el ejercicio seleccionamos us-central-1 y en la 
####     la disponibilidad zonal seleccionamos la opción : Zona única
#### 1.6 Damos clic en "CREAR INSTANCIA"

### 2 Crear Base de Datos
#### 2.1. Ir al menu "INSTANCIA PRINCIPAL"  y seleccionar la opción "Base de datos"
#### 2.2. Clic en el botón "CREAR BASE DE DATOS"
#### 2.3. Ingresar el nombre de la base de datos , para el ejercio usaremos el nombre
####      "bd-sql-1"
#### 2.4. Dar clic en el botón "CREAR"


### 3 Ejecutar script's SQL

#### 3.1 Habilitar la API de cloud SQL
gcloud services enable sqladmin.googleapis.com

#### 3.2 Ir el Menu de "INSTANCIA PRINCIPAL"
#### 3.3 Seleccionar la opción  "Descripción general"
#### 3.4 Buscar el botón "ABRIR CLOUD SHELL"
#### 3.5 Se abrirá el terminal de cloud shell con el comando de conexión 
####     donde pedirá la clave .

#### 3.6 Ejecutar las siguientes sentencias SQL : 
use bd-sql-1

create table customer (id int , name varchar(100) , gender char(1));

insert into customer (id,name,gender) values (1,'Juan Perez','M');
insert into customer (id,name,gender) values (2,'Maria del Rio','F');

select * from customer;

### 4 Integrar con Cloud Storage
#### 4.1 Clonar el repositorio
git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/sql/demo

#### 4.2. para agregar la IP que va a leer la base de datos 
####      tenemos que agregarlo a Cloud SQL, identificar 
####      tu ip en la siguiente página :

https://whatismyipaddress.com/es/mi-ip


#### 4.3. Editar la instancia 
#### 4.4 Ir a la sección Conexiones y agregar tu IP.
#### 4.5 Dar clic en Guardar 
