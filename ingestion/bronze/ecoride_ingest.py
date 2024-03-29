from ingestion.utils.spark_utils import create_spark_session
from ingestion.utils.data_ingestor import DataIngestor
from ingestion.utils.config_loader import ConfigLoader
from ingestion.utils.file_path_manager import FilePathManager

if __name__ == "__main__":
    config = ConfigLoader()
    spark = create_spark_session()
    ingestor = DataIngestor(spark)
    path_manager = FilePathManager(config.base_data_dir, config.bronze_s3_path)

    # Ingest ecoride_customers.csv to the Bronze layer
    customer_file = path_manager.get_local_file_path("ecoride_customers", "csv")
    customer_s3_path = path_manager.get_bronze_s3_path("ecoride", "customers")
    ingestor.ingest_file_to_bronze(customer_file, customer_s3_path, "csv")

    # Ingest ecoride_sales.csv to the Bronze layer
    sales_file = path_manager.get_local_file_path("ecoride_sales", "csv")
    sales_s3_path = path_manager.get_bronze_s3_path("ecoride", "sales")
    ingestor.ingest_file_to_bronze(sales_file, sales_s3_path, "csv")

    # Ingest ecoride_vehicles.csv to the Bronze layer
    vehicles_file = path_manager.get_local_file_path("ecoride_vehicles", "csv")
    vehicles_s3_path = path_manager.get_bronze_s3_path("ecoride", "vehicles")
    ingestor.ingest_file_to_bronze(vehicles_file, vehicles_s3_path, "csv")

    # Ingest ecoride_product_reviews.json to the Bronze layer
    reviews_file = path_manager.get_local_file_path("ecoride_product_reviews", "json")
    reviews_s3_path = path_manager.get_bronze_s3_path("ecoride", "product_reviews")
    ingestor.ingest_file_to_bronze(reviews_file, reviews_s3_path, "json")

