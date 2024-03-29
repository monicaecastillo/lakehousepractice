from pyspark.sql import SparkSession
from dotenv import load_dotenv
import os

# Load .env file. This line assumes the .env file is in the parent directory of the script
load_dotenv(os.path.join(os.path.dirname(__file__), '../..', '.env'))

def create_spark_session():
    """Create a Spark session configured for MinIO."""
    return SparkSession.builder \
        .appName("EcoRide Data Ingestion to Bronze") \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262") \
        .config("spark.hadoop.fs.s3a.endpoint", os.environ.get("AWS_S3_ENDPOINT")) \
        .config("spark.hadoop.fs.s3a.access.key", os.environ.get("AWS_ACCESS_KEY_ID")) \
        .config("spark.hadoop.fs.s3a.secret.key", os.environ.get("AWS_SECRET_ACCESS_KEY")) \
        .config("spark.hadoop.fs.s3a.path.style.access", True) \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .getOrCreate()

