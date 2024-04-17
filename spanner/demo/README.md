
### Procedimiento para desplegar 


### 1. Crear Instancia 

#### 1.1. Ir al menú de navegación de cloud Console , en base de datos haga 
#### clic en Spanner

#### 1.2. Luego haga clic en el botón "CREAR UNA INSTANCIA PROVISIONADA"

#### 1.3 Ingresar el nombre de la instancia 

#### 1.4 Selecciona la Ubicación 
#### 1.5 Configura la capacidad de procesamiento

### 2. Crear una Base de datos 

#### 2.1. Desde el panel "Descripción General" , buscar y dar clic al botón 
#### "CREAR BASE DE DATOS"
#### 2.2. Ingresar el nombre de la base de datos , para el ejemplo usar "test-bd-spanner"
#### 2.3. Dar clic en el botón "CREAR"


### 3. Crear una tabla en tu base de datos

#### 3.1. Ir al detalle de la base de datos "test-bd-spanner"
#### 3.2. Clic en el botón "CREAR TABLA" 
#### 3.3. Despues de dar clic se abrirá el la herramienta Spanner Studio ,
###       En el editor ejecutar el siguiente script SQL :

CREATE TABLE Customer (
  CustomerId STRING(36) NOT NULL,
  Name STRING(MAX) NOT NULL,
  Location STRING(MAX) NOT NULL,
) PRIMARY KEY (CustomerId);

### 4. Insertar datos
#### En Spanner Studio , ejecutar el siguiente script :

INSERT INTO
  Customer (CustomerId,
    Name,
    Location)
VALUES
  ('bdaaaa97-1b4b-4e58-b4ad-84030de92235',
    'Richard Nelson',
    'Ada Ohio'
    );

INSERT INTO
  Customer (CustomerId,
    Name,
    Location)
VALUES
  ('b2b4002d-7813-4551-b83b-366ef95f9273',
    'Shana Underwood',
    'Ely Iowa'
    );




### 5. Usando CLI

#### 5.1. Crear Instancia
 gcloud spanner instances create [INSTANCE-ID] \
    --config=[INSTANCE-CONFIG] \
    --description="[INSTANCE-NAME]" \
    --nodes=[NODE-COUNT]

#### 5.2. Ingresamos los valores a las variables , para 
####      el ejemplo usaramos el siguiente  comando

gcloud spanner instances create test-bd-spanner-2 \
--config=regional-  \
--description="test-bd-spanner" \
--nodes=2

#### 5.3 Listar Instancias 

gcloud spanner instances list

#### 5.4 Crear base de datos
gcloud spanner databases create retail-db-2 --instance=test-bd-spanner-2

#### 5.5 Modificando el número de nodos

gcloud spanner instances update test-bd-spanner-2 --nodes=1




#### Integrar datos de Cloud Spanner

gcloud services enable spanner.googleapis.com




