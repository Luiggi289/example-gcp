from google.cloud import spanner
import pandas as pd
from google.cloud import storage



# Configura los detalles de la base de datos y la tabla de Cloud Spanner
project_id='premium-guide-410714' 
instance_id = 'test-spanner'
database_id = 'test-bd-spanner'
table_name = 'Customer'

# Configura el nombre del archivo CSV que se guardará en Cloud Storage
bucket_name = 'test-nh'
file_name = 'customer_spanner.csv'

# Configura la ruta de destino en Cloud Storage
destination_blob_name = f'spanner/{file_name}'

# Configura el cliente de Cloud Spanner
spanner_client = spanner.Client(project=project_id)
instance = spanner_client.instance(instance_id)
database = instance.database(database_id)

# Consulta los datos de la tabla de Cloud Spanner
with database.snapshot() as snapshot:
    results = snapshot.execute_sql(f'SELECT * FROM {table_name}')

# Convierte los resultados a un DataFrame de Pandas
df = pd.DataFrame(results)


# Configura el cliente de Cloud Storage
storage_client = storage.Client(project=project_id)
bucket = storage_client.bucket(bucket_name)

# Sube el Dataframe a Cloud Storage
blob = bucket.blob(destination_blob_name)
blob.upload_from_string(df.to_csv(index=False), content_type='text/csv')



print(f'Archivo CSV guardado en Cloud Storage: gs://{bucket_name}/{destination_blob_name}')