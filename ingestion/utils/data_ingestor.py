from pyspark.sql import SparkSession
import logging

class DataIngestor:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def create_or_replace_iceberg_table(self, df, business_entity, table_name):
        # Generate SQL statement for table creation
        schema = df.schema
        schema_sql = ', '.join([f"{field.name} {field.dataType.simpleString()}" for field in schema.fields])
        create_table_sql = f"CREATE OR REPLACE TABLE nessie.{business_entity}_{table_name} ({schema_sql}) USING iceberg"

        # Execute the SQL statement
        try:
            self.spark.sql(create_table_sql)
            logging.info(f"Iceberg table nessie.{business_entity}_{table_name} created/replaced successfully.")
        except Exception as e:
            logging.error(f"Error creating/replacing Iceberg table: {e}")
            raise e


    def ingest_file_to_bronze(self, file_path: str, business_entity: str, table_name: str, file_type: str):
        try:
            if file_type == 'csv':
                df = self.spark.read.csv(file_path, header=True, inferSchema=True)
            elif file_type == 'json':
                df = self.spark.read.option("multiLine", "true").json(file_path)
            else:
                raise ValueError(f"Unsupported file type '{file_type}'. Supported types: csv, json")

            # Construct the full table path
            full_table_path = f"nessie.{business_entity}_{table_name}"

            # Ensure the Iceberg table exists
            self.create_or_replace_iceberg_table(df, business_entity, table_name)

            # Write data to Iceberg table
            df.write.format("iceberg").mode("overwrite").save(full_table_path)
            logging.info(f"Data ingested successfully from {file_path} to Iceberg table {full_table_path}")
        
        except Exception as e:
            logging.error(f"Error in ingesting file to Iceberg table: {e}")
            raise e


