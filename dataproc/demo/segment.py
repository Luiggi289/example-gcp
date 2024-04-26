#!/usr/bin/env python

"""BigQuery I/O PySpark example."""

from pyspark.sql import SparkSession
from pyspark.sql.functions import datediff, max as spark_max, min as spark_min, expr, percentile_approx
spark = SparkSession \
  .builder \
  .config("spark.jars.packages", "com.google.cloud.spark:spark-3.5-bigquery-0.37.0") \
  .master('yarn') \
  .appName('spark-bigquery-segmentaction') \
  .getOrCreate()


# Use the Cloud Storage bucket for temporary BigQuery export data used
# by the connector.
bucket = "premium-guide-410714-dataproc-tmp"
spark.conf.set('temporaryGcsBucket', bucket)

# Load data from BigQuery.
df = spark.read.format('bigquery') \
  .option('table', 'premium-guide-410714:datamart_ventas.input_segmentacion') \
  .load()


print(df.columns)

# Calcular la diferencia en días por cliente

tendencia_ventas = df.groupBy("user_id") \
    .agg(datediff(spark_max("order_date"), spark_min("order_date")).alias("dias_compra"))


# Calcular percentiles
percentiles = tendencia_ventas.stat.approxQuantile("dias_compra", [0.33, 0.66], 0.01)
corto, largo = percentiles

# Definir segmento en base a los percentiles
segmento_expr = expr("""
    CASE 
        WHEN dias_compra <= {} THEN 'Bajo'
        WHEN dias_compra <= {} THEN 'Medio'
        ELSE 'Alto'
    END AS segmento
""".format(corto, largo))

# Aplicar la segmentación
segmentacion = tendencia_ventas.withColumn("segmento", segmento_expr)


segmentacion.write \
.format("bigquery") \
.option("temporaryGcsBucket",bucket) \
.save("datamart_ventas.bi_segmentacion")