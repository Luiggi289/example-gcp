import pandas as pd
from google.cloud import bigquery
import functions_framework


@functions_framework.http
def load(request):
    headers_files = {
    'tipocambio':["fecha","compra","venta","nn"]
    }
    dwn_url_tipcambio='https://www.sunat.gob.pe/a/txt/tipoCambio.txt'
    tipcambio_df = pd.read_csv(dwn_url_tipcambio, names=headers_files['tipocambio'], sep='|')


    tipcambio_df = tipcambio_df.drop(columns=['nn'])

    client = bigquery.Client()

    table_id =  "premium-guide-410714.dep_raw.exchange_rate_v2"
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("fecha", bigquery.enums.SqlTypeNames.STRING),
            bigquery.SchemaField("compra", bigquery.enums.SqlTypeNames.FLOAT),
            bigquery.SchemaField("venta", bigquery.enums.SqlTypeNames.FLOAT),
        ],
        write_disposition="WRITE_TRUNCATE",
    )


    job = client.load_table_from_dataframe(
        tipcambio_df, table_id, job_config=job_config
    )  
    job.result()  # Wait for the job to complete.

    table = client.get_table(table_id)  # Make an API request.
    print(
        "Loaded {} rows and {} columns to {}".format(
            table.num_rows, len(table.schema), table_id
        )
    )
