from database_connection import DatabaseConnection
from validate_data import data_missing_from_row, log_invalid_row


def load_new_data(extracted_data, table_name):
    # InitialiSe a connection to the database
    db_connection = DatabaseConnection()
    db_connection.connect()
    print("database connection successful")

    # Get column names from the first row of extracted data
    column_names = extracted_data[0].keys()

    # Define columns with data types for table creation (all columns as VARCHAR(100))
    column_definitions = ", ".join(
        [f"{column_name} VARCHAR(100)" for column_name in column_names]
    )

    # Drop the table if it already exists to avoid duplicate data
    db_connection.execute(f"DROP TABLE IF EXISTS {table_name}")

    # Create a new table with an 'id' primary key and columns based on the extracted data
    db_connection.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} (id SERIAL PRIMARY KEY, {column_definitions})"
    )

    # Prepare column names and placeholders for the insert query
    column_names = ", ".join(column_names)
    values_placeholder = ", ".join(["%s" for _ in column_names.split(", ")])

    # Insert each row of data into the table
    for row in extracted_data:
        # Check if there is missing data in the row
        if data_missing_from_row(row, extracted_data[0].keys()):
            # Log invalid rows that have missing data
            log_invalid_row(table_name, row)
        else:
            # Insert valid row data into the table
            query = f"INSERT INTO {table_name} ({column_names}) VALUES ({values_placeholder})"
            db_connection.execute(
                query,
                tuple(row[column_name] for column_name in column_names.split(", ")),
            )

    # Print the count of invalid rows logged in the 'invalid_data' table
    print(len(db_connection.execute("SELECT * FROM invalid_data")))

    # Return a success message after all data has been processed
    return "Data loaded successfully"
