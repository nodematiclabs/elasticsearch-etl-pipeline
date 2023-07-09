from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
import pyspark.sql.functions as F

# Create a Spark session
spark = SparkSession.builder \
    .appName("ElasticsearchToPostgres") \
    .config("spark.jars.packages", "org.elasticsearch:elasticsearch-hadoop:7.10.0,org.postgresql:postgresql:42.2.5") \
    .getOrCreate()

# Define the Elasticsearch configuration
es_conf = {
    "es.nodes": "REPLACE ME",
    "es.port": "9200",
    "es.net.http.auth.user": "elastic",
    "es.net.http.auth.pass": "REPLACE ME",
    "es.resource": "test-index",
    "es.nodes.discovery": "true",
    "es.nodes.client.only": "false"
}

# Create a DataFrame that represents data in Elasticsearch
es_stream_df = spark.read \
    .format("es") \
    .options(**es_conf) \
    .load()

# Add a date field based on the timestamp
es_stream_df = es_stream_df.withColumn("date", F.to_date(F.col("timestamp"), "yyyy-MM-dd"))

# Define PostgreSQL configuration
pg_properties = {
    "user": "postgres",
    "password": "REPLACE ME",
    "driver": "org.postgresql.Driver",
}

pg_url = "jdbc:postgresql://REPLACE ME:5432/elastic"

# Write the DataFrame to PostgreSQL
query = es_stream_df.write \
    .format("jdbc") \
    .mode("append") \
    .option("url", pg_url) \
    .option("dbtable", "data") \
    .options(**pg_properties) \
    .save()