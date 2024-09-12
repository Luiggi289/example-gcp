### Sintaxis YAML

```
https://cloud.google.com/workflows/docs/reference/syntax
```
### * Importante : La identación es fundamental ya que se utiliza para indicar la estructura jerárquica de los dato.

### Main 

#### El flujo de trabajo principal es el punto de entrada de tu definición de flujo de trabajo y
#### contiene los pasos que se ejecutarán en secuencia cuando se inicie el flujo de trabajo :

#### Ejemplo :
```
  main:
      params: [MAP_NAME]
      steps:
          - STEP_NAME:
```
#### * Params : Son valores que pueden ser pasados al flujo de trabajo cuando se inicia su ejecución .

### Step 

#### Para crear un flujo de trabajo, define los pasos que desea y su orden de ejecución utilizando 
#### la sintaxis de Flujos de trabajo. Cada flujo de trabajo debe tener al menos un paso.
#### Ejemplo : 
```
  - STEP_NAME_A:
      ...
  - STEP_NAME_B:
      ...
```

### Call
#### se utiliza para invocar una función o un servicio externo como parte de un paso dentro de un flujo 
#### de trabajo. Específicamente, call se utiliza para definir una llamada a una función de 
#### Google Cloud (Conectores)  o una solicitud HTTP a una API externa.
```
  - STEP_NAME:
      call: FUNCTION_NAME
      args:
          ARG_1: VALUE_1
          ARG_2: VALUE_2
          ...
      result: OUTPUT_VARIABLE
```

#### Conectores :
```
https://cloud.google.com/workflows/docs/reference/googleapis
```

#### Solicitudes HTTP :
```
http.delete
http.get
http.patch
http.post
http.put
http.request
```
#### Ejemplo Solicitud HTTP :
```
- get_message:
    call: http.post
    args:
      url: https://www.example.com/endpoint
      body:
        some_val: "Hello World"
        another_val: 123
    result: the_message
- return_value:
    return: ${the_message.body}
```


### Variables
### La variable los puedes asignar en el paso de un flujo de trabajo o asignarlos como resultado de un paso de call  
```
  - STEP_NAME:
      assign:
          - VARIABLE_NAME: VALUE
```

#### Ejemplo : 
```
  - assign_vars:
      assign:
          - number: 5
          - number_plus_one: ${number+1}
          - other_number: 10
          - string: "hello"
```


### Creando Workflows

#### 1.- Ir Cloud Shell y Habilitar el workflow de GCP con el siguiente comando :
```
gcloud services enable workflows.googleapis.com
```
#### 1.1 Clonar repositorio
```
cd
rm -r example-gcp -f
git clone https://github.com/Luiggi289/example-gcp.git  
cd example-gcp/workflows/demo
```
#### 1.2 Copiar archivo
```
gsutil cp tipo_cambio.csv gs://premium-guide-410714-datalake-dev/sunat/tipo_cambio.csv
```


#### 2.- crear dataset donde se guardaran los datos  
#### 2.1.- Ir a Bigquery y ejecutar el siguientes script :

```
CREATE SCHEMA IF NOT EXISTS `[project_id].raw_taller_ventas`  

  OPTIONS (    location = 'US'); 
```
#### 2.2 Crear el procedure de carga en Bigquery
```
CREATE OR REPLACE PROCEDURE `[project_id].raw_taller_ventas.sp_load_exchange_rate`()
BEGIN

LOAD DATA OVERWRITE   `[project_id].raw_taller_ventas.tipo_cambio` 
FROM FILES (
  format = 'CSV',
  uris = ['gs://premium-guide-410714-datalake-dev/sunat/tipo_cambio.csv']);
END 
;
```


#### 3.- Ir a la consola de GCP y buscar el producto workflows
#### 4.- Clic en el botón Crear 
#### 5.- En el campo "Nombre del flujo de trabajo" ingresar el valor : 

```
workflow-carga-taller-dmventa
```
#### 5.- En Región seleccionamos la opción us-central1
#### 6.- En cuenta de servicio seleccionamos a cuenta de servicio por defecto
#### 7.- Clic en siguiente 
#### 8.- Pegar el siguiente código 



```
main:
    params: [input]
    steps:
    - InitVariables:
        assign:
            - bq_project_id: premium-guide-410714

    - load_bq_raw_tipo_cambio:
        call: googleapis.bigquery.v2.jobs.query
        args:
          body:
            query: ${"CALL `"+bq_project_id+".raw_taller_ventas.sp_load_exchange_rate`()"}
            useLegacySql: false
          projectId: ${bq_project_id}
        result: queryResult
```

#### 9.- Dar clic en implementar

#### 10 Brindar los siguientes accesos a la cuenta de servicio que se configuró en el flujo de trabajo
#####   Acceso de Bigquery Data Editor en el dataset en el dataset  [project_id].raw_taller_ventas
#####   Visualizador de objetos de Storage en el bucket donde está el archivo tipo_cambio.csv
#####   Usuario de trabajo de Bigquery en el Proyecto

