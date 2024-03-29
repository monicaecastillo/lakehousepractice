from pyspark.sql import SparkSession
import logging

class DataIngestor:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def ingest_file_to_bronze(self, file_path: str, minio_output_path: str, file_type: str):
        try:
            if file_type == 'csv':
                df = self.spark.read.csv(file_path, header=True, inferSchema=True)
            elif file_type == 'json':
                df = self.spark.read.option("multiLine", "true").json(file_path)
            else:
                raise ValueError(f"Unsupported file type '{file_type}'. Supported types: csv, json")

            df.write.mode("overwrite").format(file_type).save(minio_output_path)
            logging.info(f"Data ingested successfully from {file_path} to {minio_output_path}")
        
        except Exception as e:
            logging.error(f"Error in ingesting file: {e}")
            raise e