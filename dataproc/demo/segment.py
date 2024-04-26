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


# Calcular las ventas totales por cliente y fecha
ventas_por_cliente = df.groupBy("user_id", "order_date") \
    .agg({"sale_price": "sum"}) \
    .withColumnRenamed("sum(sale_price)", "total_venta")

# Calcular la diferencia en días y el cambio en las ventas por cliente
tendencia_ventas = ventas_por_cliente.groupBy("user_id") \
    .agg(datediff(spark_max("order_date"), spark_min("order_date")).alias("dias_compra"),
         (spark_max("total_venta") - spark_min("total_venta")).alias("cambio_venta"))

# Calcular los percentiles para la segmentación
percentiles = tendencia_ventas.selectExpr("percentile_approx(dias_compra, 0.33)", 
                                          "percentile_approx(dias_compra, 0.66)",
                                          "percentile_approx(cambio_venta, 0.33)",
                                          "percentile_approx(cambio_venta, 0.66)") \
                               .collect()[0]

corto, largo, negativo, neutro = percentiles

# Definir expresiones para las condiciones de segmentación
segmento_expr = expr("""
    CASE 
        WHEN dias_compra <= {} AND cambio_venta <= {} THEN 'Bajo y Disminuyendo'
        WHEN dias_compra <= {} AND cambio_venta > {} AND cambio_venta <= {} THEN 'Bajo y Estable'
        WHEN dias_compra <= {} AND cambio_venta > {} THEN 'Bajo y Aumentando'
        WHEN dias_compra > {} AND dias_compra <= {} AND cambio_venta <= {} THEN 'Medio y Disminuyendo'
        WHEN dias_compra > {} AND dias_compra <= {} AND cambio_venta > {} AND cambio_venta <= {} THEN 'Medio y Estable'
        WHEN dias_compra > {} AND dias_compra <= {} AND cambio_venta > {} THEN 'Medio y Aumentando'
        WHEN dias_compra > {} AND cambio_venta <= {} THEN 'Alto y Disminuyendo'
        WHEN dias_compra > {} AND cambio_venta > {} AND cambio_venta <= {} THEN 'Alto y Estable'
        ELSE 'Alto y Aumentando'
    END AS segmento
""".format(corto, negativo, corto, negativo, neutro, corto, neutro,
           corto, largo, negativo, largo, negativo, neutro, largo, neutro,
           largo, negativo, largo, negativo, neutro))

# Aplicar la segmentación
segmentacion = tendencia_ventas.withColumn("segmento", segmento_expr)




segmentacion.write \
.format("bigquery") \
.option("temporaryGcsBucket",bucket) \
.save("datamart_ventas.bi_segmentacion")