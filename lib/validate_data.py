from database_connection import DatabaseConnection


def data_missing_from_row(data_row, required_fields):
    for item in required_fields:
        if data_row[item] == "" or data_row[item] == None:
            return True
    return False


def log_invalid_row(table_name, row):
    db_connection = DatabaseConnection()
    db_connection.connect()
    db_connection.execute(
        f"CREATE TABLE IF NOT EXISTS invalid_data (id SERIAL PRIMARY KEY, intended_table VARCHAR(100), row_contents VARCHAR(100), reason VARCHAR(100), missing_fields VARCHAR(100))"
    )
    query = f"SELECT * FROM invalid_data WHERE row_contents = %s"
    result = db_connection.execute(query, (str(row),))
    if not result:
        query = f"INSERT INTO invalid_data (intended_table, row_contents, reason, missing_fields) VALUES (%s, %s, %s, %s)"
        db_connection.execute(
            query,
            (
                table_name,
                str(row),
                "Data missing from row",
                [item for item in row.keys() if row[item] == ""],
            ),
        )
