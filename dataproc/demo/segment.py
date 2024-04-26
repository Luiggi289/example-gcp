#!/usr/bin/env python

"""BigQuery I/O PySpark example."""

from pyspark.sql import SparkSession

spark = SparkSession \
  .builder \
  .config("spark.jars.packages", "com.google.cloud.spark:spark-3.5-bigquery-0.37.0") \
  .master('yarn') \
  .appName('spark-bigquery-demo') \
  .getOrCreate()


# Use the Cloud Storage bucket for temporary BigQuery export data used
# by the connector.
bucket = "premium-guide-410714-dataproc-tmp"
spark.conf.set('temporaryGcsBucket', bucket)

# Load data from BigQuery.
words = spark.read.format('bigquery') \
  .option('table', 'bigquery-public-data:samples.shakespeare') \
  .load()

print(words.columns)

word_count = spark.sql('SELECT word, SUM(word_count) AS word_count FROM words GROUP BY word')

word_count.write.format('bigquery') \
  .option('table', 'wordcount_dataset.wordcount_output') \
  .save()
