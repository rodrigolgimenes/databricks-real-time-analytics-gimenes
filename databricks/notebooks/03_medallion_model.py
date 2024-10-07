# Load data from Silver layer
silver_data = spark.read.format("delta").load("/delta/silver/cross_referenced_data")

# Perform enrichment and aggregation
gold_data = silver_data.groupBy("campaign").agg(
    sum("clicks").alias("total_clicks"),
    sum("impressions").alias("total_impressions")
)

# Write enriched and aggregated data to Gold layer
gold_data.write.format("delta").mode("overwrite").save("/delta/gold/campaign_performance")
