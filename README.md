# FutureMobility EVs Data Lakehouse Capstone Project

## About the Project
This project demonstrates the construction of a data lakehouse focused on a mock company, "FutureMobility EVs". FutureMobility is a fictional company that specializes in electric vehicles and charging solutions. The project showcases various aspects of data engineering, including data ingestion, storage, processing, and analysis, using open-source tools.

## Mock Data Description

This project uses mock data to represent various aspects of the fictional company. Each dataset serves a specific purpose in demonstrating the functionality of the data lakehouse.

### EcoRide Vehicles
- **Dataset**: Vehicle Models and Specifications
- **Data Points**: Vehicle details including model, battery capacity, range, and price.
- **Format**: Structured (CSV)
- **Use**: Understanding vehicle diversity, pricing strategies, and customer preferences.

### EcoRide Sales
- **Dataset**: Vehicle Sales Transactions
- **Data Points**: Sales data capturing transaction details, customer and vehicle IDs, dates, and prices.
- **Format**: Structured (CSV)
- **Use**: Sales trend analysis, revenue forecasting, customer buying behavior.

### EcoRide Customers
- **Dataset**: Customer Profiles
- **Data Points**: Customer information including demographic details, contact info, and purchasing history.
- **Format**: Structured (CSV)
- **Use**: Customer segmentation, personalized marketing, customer relationship management.

### ChargeNet Stations
- **Dataset**: EV Charging Station Data
- **Data Points**: Station IDs, locations, capacity, and type.
- **Format**: Structured (JSON)
- **Use**: Charging infrastructure analysis, station utilization, and maintenance planning.

### ChargeNet Charging Sessions
- **Dataset**: EV Charging Session Logs
- **Data Points**: Session details including IDs, timings, energy consumed, and vehicle information.
- **Format**: Structured (JSON)
- **Use**: Analyzing charging patterns, optimizing energy distribution, usage-based billing.

### Product Reviews
- **Dataset**: Customer Reviews of EcoRide Vehicles
- **Data Points**: Review IDs, vehicle models, customer feedback, ratings, and review texts.
- **Format**: Semi-structured (JSON)
- **Use**: Sentiment analysis, product improvement, customer satisfaction tracking.

### Vehicle Health Data
- **Dataset**: Vehicle Performance and Maintenance Records
- **Data Points**: Vehicle maintenance logs, performance metrics, service flags, and battery health.
- **Format**: Semi-structured (JSON)
- **Use**: Predictive maintenance, performance optimization, vehicle health monitoring.

### PDF Documents

Apart from the structured and semi-structured datasets, this project also incorporates a range of PDF documents. These include:

1. **Technical Specifications Sheets**: Detailed specs for each EcoRide EV model.
2. **Vehicle Comparison Brochure**: Comparative analyses of different EcoRide EV models, highlighting their features and benefits.
3. **Maintenance Tips Sheets**: Guides and tips for maintaining the health and performance of EcoRide EVs.

These PDFs serve as a rich source of information for a Large Language Model (LLM) application, enabling it to provide detailed responses based on extensive product knowledge.

Each dataset is synthetically generated to simulate real-world scenarios, showcasing the capabilities of a data lakehouse in handling diverse data types and formats.

## Installation

### Prerequisites

Before you get started with this project, make sure you have the following installed:

1. **Java**: The Spark framework requires Java to be installed on your system. Make sure you have at least Java 8 or higher.

2. **Python**: This project is developed using Python. Ensure you have Python 3.9 or newer.

3. **Docker**: Since the project uses Docker for running services like MinIO, Dremio, and Nessie, Docker must be installed. Download Docker from [Docker's official site](https://www.docker.com/get-started).

### Installation Steps
1. **Clone the Repository**:
   ```
   git clone https://github.com/ThaliaBarrera/lakehouse-capstone.git
   ```

2. **Navigate to the Project Directory**:
   ```
   cd lakehouse-capstone
   ```

3. **Build and Run Docker Containers**:
   - Ensure Docker is running on your machine.
   - Execute the following command to build and run the necessary services (MinIO, Dremio and Nessie):
     ```
     docker-compose up -d
     ```
4. **Access MinIO**:
    - Go to http://localhost:9000 in your browser and login to the MinIO UI using the credentials defined in the `docker-compose.yml` file.
    - Create a new access key in the `Acesss Keys` section.
        - Update the `.env.example` file with your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
    - Create a bucket named `lakehouse`

5. **Access Dremio and Connect to MinIO and Nessie**:
    - Go to http://localhost:9047 in your browser and create a new account if you don't have one. Then, log into your account.
    - Click on "Add Source" at the bottom left, and select "Nessie" under "Catalogs".
    - In the "General" tab, fill in the details like "Name", "Endpoint" (`http://nessie:19120/api/v2`) and select "None" as the authetication type.
    - Then, go to the "Storage" tab and fill in the details:
      - The "AWS root path" should point to `lakehouse`.
      - Select AWS Access Key as the auth method and fill in with your "AWS Access Key", "AWS Access Secret".
      - Add 3 new "Connection Properties":
        - `fs.s3a.endpoint`: `minio:9000`
        - `fs.s3a.path.style.access`: `true`
        - `dremio.s3.compat`: `true`
    - Click "Save".

6. **Install Python Dependencies**:
   - It's recommended to create a virtual environment:
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows: `.\venv\Scripts\activate`
     - On Linux/Mac: `source venv/bin/activate`
     
   - Install required packages:
     ```
     pip install -r requirements.txt
     ```

5. **Setting Up Environment Variables**:
   - Copy the `.env.example` file to create a `.env` file (or just rename it):
     ```
     cp .env.example .env
     ```
   - Make sure all the environment variables are correct.

## Project Usage

1. **Data Ingestion**:
   - Run the ingestion scripts to populate data into the data lakehouse:
     ```
     python -m ingestion.bronze.ecoride_ingest
     python -m ingestion.bronze.chargenet_ingest
     python -m ingestion.bronze.vehicle_health_ingest
     ```
2. **Data Transformation**:
  The data transformations are handed by `dbt`. The `dbt` project is in the `lakehouse` folder. Before running the transformations, a couple of assets need to be created in Dremio.

  - Go to the Dremio UI, and click on the Nessie `catalog` in Sources.
  - Create a new folder named `silver` inside the catalog. This will create a namespace with the same name in Nessie. This folder will hold the tables corresponding to the silver layer.
  - In the Spaces section, create a new space named `lakehouse` and inside, create a folder named `gold`. These will hold the views created by `dbt`.
  - In the terminal, move to the `lakehouse` directory:
    ```
    cd lakehouse
    ```
  - Create 2 new environment variables, `DREMIO_USER` and `DREMIO_PASSWORD` and assign the values of your user and password. These variables are used by the `profiles.yml` file to allow `dbt` to connect to Dremio.
  - Verify that `dbt` can connect to Dremio and everything is set up correctly:
    ```
    dbt debug
    ```
  - Run the models:
    ```
    dbt run --target silver --models tag:silver
    dbt run --target gold --models tag:gold
    ```
  The silver models should be materialized as tables inside the `catalog`, and the gold models as views in the `lakehouse/gold` space.

2. **Data Exploration and Analysis**:

## Contributing

## License

## Contact
