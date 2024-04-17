import pandas as pd
import sqlalchemy as db
from sqlalchemy import text
from google.cloud import storage

engine = db.create_engine("mysql+pymysql://root:EM7{$'Oru|&aB{>#@104.197.207.218/bd-sql-1")
conn = engine.connect()

df = pd.read_sql_query(text('SELECT * FROM customer'), con=conn)
conn.close()


project_id='premium-guide-410714'

# Configura el nombre del archivo CSV que se guardará en Cloud Storage
bucket_name = 'test-nh'
file_name = 'output.csv'
destination_blob_name = f'sql/{file_name}'

# Configura el cliente de Cloud Storage
storage_client = storage.Client(project=project_id)
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)
# Sube el archivo CSV temporal a Cloud Storage
blob.upload_from_string(df.to_csv(index=False), content_type='text/csv')


print(f'Archivo CSV guardado en Cloud Storage: gs://{bucket_name}/{destination_blob_name}')
