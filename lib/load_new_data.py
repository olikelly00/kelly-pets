from database_connection import DatabaseConnection
from validate_data import data_missing_from_row, log_invalid_row


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
        if data_missing_from_row(row, extracted_data[0].keys()):
            log_invalid_row(table_name, row)
        else:
            query = f"INSERT INTO {table_name} ({column_names}) VALUES ({values_placeholder})"
            db_connection.execute(query, tuple(row[column_name] for column_name in column_names.split(", ")))    
    print(len(db_connection.execute("SELECT * FROM invalid_data")))
    return "Data loaded successfully"




