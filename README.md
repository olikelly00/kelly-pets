KellyPets Data Pipeline
=======================

**KellyPets** is a project where I built a fully functioning data pipeline from scratch, designed to ingest, validate, and load data related to pets, their insurance policies, and vet visits. The project supports data ingestion from multiple sources, including CSV, XLSX, and JSON, and automates data loading into a database. This project serves as a foundational step in learning how to build scalable data pipelines that can efficiently process and store data from different formats.

Features
--------

-   Ingestion of pet-related data from various formats: CSV, XLSX, and APIs.
-   Data validation and handling of missing or invalid fields.
-   Automated loading of clean data into a SQL database.
-   Integration with a companion API for mocking JSON data: [Kelly Vets API](https://github.com/olikelly00/kelly-vets-api)

Project Structure
-----------------
`kelly_pets/
│
├── lib/
│   ├── database_connection.py       # Handles database connection logic
│   ├── ingest_from_api.py           # Function to ingest data from APIs
│   ├── ingest_from_csv.py           # Function to ingest data from CSV
│   ├── ingest_from_xlsx.py          # Function to ingest data from XLSX
│   ├── ingest_new_data.py           # Main data ingestion logic
│   ├── load_new_data.py             # Logic to load data into the database
│   └── validate_data.py             # Data validation logic
│
├── mock_data/                       # Directory for mock datasets
│   ├── claim_details.json           # Mock claim details in JSON format
│   ├── missing_pet_details.csv      # CSV file with missing fields for validation tests
│   ├── pet_details.csv              # Complete pet details CSV
│   └── policy_data.xlsx             # Insurance policy details in XLSX format
│
└── tests/                           # Unit tests for different components
    ├── test_ingest_from_api.py      # Test for API ingestion
    ├── test_ingest_from_csv.py      # Test for CSV ingestion
    ├── test_ingest_from_xlsx.py     # Test for XLSX ingestion
    ├── test_ingest_new_data.py      # Test for ingesting all formats
    ├── test_load_new_data.py        # Test for loading data into the database
    └── test_validate_data.py        # Test for validating missing data`

Getting Started
---------------

### Prerequisites

Ensure you have the following installed:

-   Python 3.7+
-   PostgreSQL (or another SQL database)
-   Pipenv (for managing dependencies)

### Setup Instructions

1.  **Clone the repository**:

    `git clone https://github.com/yourusername/kelly_pets.git
    
    cd kelly_pets`

3.  **Install dependencies** using Pipenv:

    `pipenv install`

4.  **Set up your local database**:

    -   Create a local PostgreSQL database to store the pet data.
    -   Update your database connection details in `database_connection.py`.
5.  **Run the tests**: You can run the unit tests to validate the functionality.

    `pipenv run pytest`

6.  **Ingest data**: You can ingest data from CSV, XLSX, and API formats using the ingestion scripts in the `lib` folder.

7.  **Mock JSON API**: To mock vet claim data, you can use the companion API project, [Kelly Vets API](https://github.com/olikelly00/kelly-vets-api). Follow the instructions in that repo to set up the API locally.

### Key Skills Developed

-   **Data Ingestion and Validation**: Learned how to handle data from multiple sources (CSV, XLSX, JSON) and ensure data quality through validation processes.
-   **Automated Data Pipelines**: Gained experience automating data ingestion and loading processes using Python and SQL, making manual data entry and cleaning redundant.
-   **Unit Testing**: Developed robust unit tests using Pytest to ensure the data ingestion logic works for all formats and catches edge cases like missing fields.
-   **Modular Code Organization**: Learned to keep code modular and readable, ensuring that each function is responsible for a specific task, which enhanced both debugging and scalability.

### Impact on My Learning

Working on **KellyPets** reinforced the importance of structuring data pipelines for scalability, accuracy, and performance. I was able to connect theoretical knowledge about data ingestion, validation, and transformation to practical implementations. By building this pipeline from scratch, I deepened my understanding of how to clean and structure data for downstream usage while considering real-world challenges like missing data. The project helped me think more critically about data quality and the importance of ensuring a seamless data flow in larger-scale applications.
