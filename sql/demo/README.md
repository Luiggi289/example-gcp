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

gcloud services enable sqladmin.googleapis.com


use bd-sql-1

create table customer (id int , name varchar(100) , gender char(1));

insert into customer (id,name,gender) values (1,'Juan Perez','M');
insert into customer (id,name,gender) values (2,'Maria del Rio','F');

select * from customer;

