
from cloudevents.http import CloudEvent
import pandas as pd
import functions_framework


# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event: CloudEvent) -> tuple:

    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")


    # Leer el archivo CSV desde Cloud Storage
    df = pd.read_csv(f"gs://{bucket}/{name}")

    # Escribir el DataFrame en BigQuery
    df.to_gbq("datamart_ventas.metas", project_id="premium-guide-410714", if_exists="replace")

    print(f"Archivo se ha cargado exitosamente a BigQuery.")


    return event_id, event_type, bucket, name, metageneration, timeCreated, updated




