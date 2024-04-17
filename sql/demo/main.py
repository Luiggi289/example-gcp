import pandas as pd
import pymysql
from google.cloud import storage

from google.cloud.sql.connector import Connector, IPTypes
import pymysql
import os
import sqlalchemy


project_id='premium-guide-410714'
# Configura los detalles de la conexión a la base de datos MySQL
mysql_config = {
    'host': '104.197.207.218',
    'user': 'root',
    'password': "EM7{$'Oru|&aB{>#" ,
    'database': 'bd-sql-1' 
}
os.environ['PRIVATE_IP'] = 'False'

instance_connection_name='premium-guide-410714:us-central1:test-bd-sql'
db_user='root'
db_pass="EM7{$'Oru|&aB{>#",
db_name= 'bd-sql-1',
# Configura el nombre de la tabla que deseas leer
table_name = 'customer'

# Configura el nombre del archivo CSV que se guardará en Cloud Storage
bucket_name = 'test-nh'
file_name = 'output.csv'

# Configura la ruta de destino en Cloud Storage
destination_blob_name = f'sql/{file_name}'

# Realiza la conexión a la base de datos MySQL
connection = pymysql.connect(**mysql_config)
#ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
#connector = Connector(IPTypes.PUBLIC)
#connection: pymysql.connections.Connection = connector.connect(
#            instance_connection_name,
#            "pymysql",
#            user=db_user,
#            password=db_pass,
#            db=db_name,
#        )

# Consulta los datos de la tabla MySQL
query = f'SELECT * FROM {table_name}'
df = pd.read_sql(query, connection)

# Cierra la conexión a la base de datos MySQL
connection.close()

# Guarda el DataFrame como un archivo CSV temporal

print(df.head())

# Configura el cliente de Cloud Storage
storage_client = storage.Client(project=project_id)
bucket = storage_client.bucket(bucket_name)

# Sube el archivo CSV temporal a Cloud Storage
blob = bucket.blob(destination_blob_name)
#blob.upload_from_filename(temp_csv_file)


print(f'Archivo CSV guardado en Cloud Storage: gs://{bucket_name}/{destination_blob_name}')
