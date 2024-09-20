from database_connection import *
from ingest_from_csv import *
from ingest_from_xlsx import *
from ingest_from_api import *
from ingest_new_data import *


def load_new_data(extracted_data, table_name):
    db_connection = DatabaseConnection()
    db_connection.connect()
    print("database connection successful")
    column_names = extracted_data[0].keys()
    column_definitions = ', '.join([f"{column_name} VARCHAR(100)" for column_name in column_names])
    db_connection.execute(f"DROP TABLE IF EXISTS {table_name}")
    db_connection.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id SERIAL PRIMARY KEY, {column_definitions})")
    column_names = ', '.join(column_names)
    values_placeholder = ', '.join(["%s" for _ in column_names.split(", ")])
    for row in extracted_data:
        query = f"INSERT INTO {table_name} ({column_names}) VALUES ({values_placeholder})"
        db_connection.execute(query, tuple(row[column_name] for column_name in column_names.split(", ")))    
    return "Data loaded successfully"


print(load_new_data(ingest_new_data('../mock_data/pet_details.csv'), 'pet_details'))
print("1 done")
print(load_new_data(ingest_new_data('../mock_data/policy_data.xlsx'), 'policy_details'))
print("2 done")
print(load_new_data(ingest_new_data('http://127.0.0.1:5000/claims'), 'claims_data'))
print("3 done")
