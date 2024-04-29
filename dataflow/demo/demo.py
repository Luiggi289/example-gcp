import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

# Definimos una función que duplica un número
def duplicar_numero(numero):
    return numero * 2

# Datos de entrada: una lista de números
numbers = [1, 2, 3, 4, 5]

gs_datalake='gs://premium-guide-410714-datalake-dev/demo/data.csv'
# Configuración de opciones de ejecución de Dataflow
options = PipelineOptions(
    project='premium-guide-410714',
    job_name='job-demo',
    staging_location='gs://premium-guide-410714-dataflow-dev',
    temp_location='gs://premium-guide-410714-dataflow-tmp-dev',
    runner='DataflowRunner',
    region='us-central1',
    max_num_workers=2,
    save_main_session=True,
)

# Creamos un pipeline de Apache Beam
with beam.Pipeline(options=options) as pipeline:
    # Creamos un PCollection con algunos números
    numeros = pipeline | beam.Create(numbers)

    # Aplicamos la transformación Map para duplicar cada número
    numeros_duplicados = numeros | beam.Map(duplicar_numero)

    # Escribimos los resultados a la salida estándar
    numeros_duplicados |  beam.io.WriteToText(gs_datalake)

    
