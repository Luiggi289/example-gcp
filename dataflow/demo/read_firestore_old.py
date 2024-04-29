import apache_beam as beam
from google.cloud import firestore
from apache_beam.options.pipeline_options import PipelineOptions
import json


gs_datalake='gs://premium-guide-410714-datalake-dev/demo/transacciones.json'

# Función para obtener datos de Firestore
def obtener_datos_firestore(documento):
    datos = documento.to_dict()  # Convertimos el documento de Firestore a un diccionario
    doc_id = documento.id  # Obtenemos el ID del documento
    
    # Extraemos los campos principales del documento
    id_cliente = datos.get('id_cliente', None)
    fecha = datos.get('fecha', None)
    local = datos.get('local', None)
    
    # Extraemos los campos anidados del documento producto
    productos = datos.get('producto', [])
    for producto in productos:
        cantidad = producto.get('cantidad', None)
        nombre_producto = producto.get('nombre', None)
        categoria = producto.get('categoria', None)
        precio = producto.get('precio', None)
        
        # Creamos un diccionario con los datos
        datos_json = {
            'id': doc_id,
            'id_cliente': id_cliente,
            'fecha': fecha,
            'local': local,
            'producto': {
                'cantidad': cantidad,
                'nombre': nombre_producto,
                'categoria': categoria,
                'precio': precio
            }
        }
        
        # Convertimos el diccionario a formato JSON y lo devolvemos con un salto de línea
        yield json.dumps(datos_json) + '\n'

# Configuración de opciones de Pipeline
options = PipelineOptions(
    project='premium-guide-410714',
    job_name='job-read-firestore',
    staging_location='gs://premium-guide-410714-dataflow-dev',
    temp_location='gs://premium-guide-410714-dataflow-tmp-dev',
    runner='DataflowRunner',
    region='us-central1',
    max_num_workers=2,
    save_main_session=True,
    extra_packages=['google-cloud-firestore==2.16.0'],
)
# Inicializamos el cliente de Firestore
db = firestore.Client()

# Creamos un pipeline de Apache Beam
with beam.Pipeline(options=options) as pipeline:
    # Consultamos la colección en Firestore
    datos_firestore = (pipeline
                       | 'Lectura de Firestore' >> beam.Create(db.collection('transacciones').stream())
                       | 'Obtener datos' >> beam.FlatMap(obtener_datos_firestore)
                       )

    # Escribimos los datos en Cloud Storage en formato JSON con saltos de línea
    datos_firestore | 'Escribir en Cloud Storage' >> beam.io.WriteToText(gs_datalake, file_name_suffix='.json')