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
   git clone https://github.com/ThaliaBarrera/ecoride-data-lakehouse.git
   ```

2. **Navigate to the Project Directory**:
   ```
   cd ecoride-data-lakehouse
   ```

3. **Build and Run Docker Containers**:
   - Ensure Docker is running on your machine.
   - Execute the following command to build and run the necessary services (like MinIO, Iceberg, Dremio, Nessie):
     ```
     docker-compose up -d
     ```

4. **Install Python Dependencies**:
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
   - Copy the `.env.example` file to create a `.env` file:
     ```
     cp .env.example .env
     ```
   - Fill in the necessary environment variables in `.env`.

## Project Usage

1. **Data Ingestion**:
   - Run the ingestion scripts to populate data into the data lakehouse:
     ```
     python -m ingestion.bronze.ecoride_ingest
     python -m ingestion.bronze.chargenet_ingest
     ```

2. **Data Exploration and Analysis**:
   - Access Dremio UI at `http://localhost:<port>` to explore and analyze the data.
   - Use Jupyter Notebooks for data analysis.

## Contributing

## License

## Contact
