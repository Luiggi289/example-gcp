import pandas as pd
import google.cloud.bigquery as bigquery
import google.cloud.storage as storage
import functions_framework

@functions_framework.http
def load_tipo_cambio(request):

    request_json = request.get_json(silent=True)
    load_type=''
    target='' 

    if request_json and 'target' in request_json:
        target = request_json['target']

    print('--------request : ',request_json)

    if request_json and 'load_type' in request_json:
        load_type = request_json['load_type']

    if load_type=='bigquery' :
        return load_tipo_cambio_bq(target)
    elif  load_type=='storage' :
        return load_tipo_cambio_st(target)
    else :
        return "no existe el tipo de carga"+ load_type

    return "tipo de carga invalido : "+ load_type    

def load_tipo_cambio_bq(target):



    headers_files = {
    'tipocambio':["fecha","compra","venta","nn"]
    }

    dwn_url_tipcambio='https://www.sunat.gob.pe/a/txt/tipoCambio.txt'
    tipcambio_df = pd.read_csv(dwn_url_tipcambio, names=headers_files['tipocambio'], sep='|')

    tipcambio_df = tipcambio_df.drop(columns=['nn'])

    client = bigquery.Client()
    table_id =  target

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


        
    return "Loaded {} rows and {} columns to {}".format(
            table.num_rows, len(table.schema), table_id
        )

def load_tipo_cambio_st(target):
    
    headers_files = {
    'tipocambio':["fecha","compra","venta","nn"]
    }

    dwn_url_tipcambio='https://www.sunat.gob.pe/a/txt/tipoCambio.txt'
    tipcambio_df = pd.read_csv(dwn_url_tipcambio, names=headers_files['tipocambio'], sep='|')

    tipcambio_df = tipcambio_df.drop(columns=['nn'])

    client = storage.Client()
    bucket = client.bucket(target.split('/')[2])
    file="/".join(target.split("/")[3:])
    blob = bucket.blob(file)
    blob.upload_from_string(tipcambio_df.to_csv(index=False), content_type='text/csv')
    return 'Tipo de cambio uploaded'

