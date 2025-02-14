import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, to_timestamp, year, month, dayofmonth, date_format

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Initialize Spark and Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Define S3 Paths (Update with actual S3 bucket names)
INPUT_PATH = "s3://twitter-raw-dev/raw/"
OUTPUT_PATH = "s3://twitter-processed-dev/processed/"

# Read the Parquet Data from S3
df = spark.read.parquet(INPUT_PATH)

# Print Schema for Debugging
df.printSchema()

# Convert `date_time` column to Timestamp Format
df_transformed = df.withColumn("date_time", to_timestamp(col("date_time"), "dd/MM/yyyy HH:mm"))

# Extract Date Parts
df_transformed = df_transformed.withColumn("day", dayofmonth(col("date_time"))) \
                               .withColumn("month", month(col("date_time"))) \
                               .withColumn("year", year(col("date_time"))) \
                               .withColumn("time", date_format(col("date_time"), "HH:mm"))

# Select the required columns
df_final = df_transformed.select(
    col("author"),
    col("content"),
    col("country"),
    col("id"),
    col("language"),
    col("latitude"),
    col("longitude"),
    col("number_of_likes"),
    col("number_of_shares"),
    col("day"),
    col("month"),
    col("year"),
    col("time")
)

# Save Transformed Data in Parquet Format to the New S3 Bucket
df_final.write.mode("overwrite").parquet(OUTPUT_PATH)

# Commit the Glue Job
job.commit()