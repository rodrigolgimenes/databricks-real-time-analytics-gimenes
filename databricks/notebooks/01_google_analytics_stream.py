from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Initialize Spark session
spark = SparkSession.builder.appName("GoogleAnalyticsStream").getOrCreate()

# Define schema for Google Analytics data
schema = StructType([
    StructField("timestamp", TimestampType(), True),
    StructField("campaign", StringType(), True),
    StructField("clicks", IntegerType(), True),
    StructField("impressions", IntegerType(), True)
])

# Read data from Google Analytics API
google_analytics_data = (
    spark.readStream.format("json")
    .schema(schema)
    .option("multiLine", True)
    .load("/path/to/google/analytics/api")
)

# Write data to Delta Lake Bronze layer
google_analytics_data.writeStream     .format("delta")     .outputMode("append")     .option("checkpointLocation", "/delta/bronze/_checkpoints/ga")     .start("/delta/bronze/google_analytics")
