import os, psycopg2 as psycopg
from psycopg2.extras import DictCursor


# This class helps us interact with the database.
# It wraps the underlying psycopg library that we are using.


class DatabaseConnection:
    # VVV CHANGE BOTH OF THESE VVV
    DEV_DATABASE_NAME = "kellypets_db"

    def __init__(self, test_mode=False):
        self.test_mode = test_mode

    # This method connects to PostgreSQL using the psycopg library.
    def connect(self):
        try:
            self.connection = psycopg.connect(
                f"postgresql://localhost/{self._database_name()}",
                cursor_factory=DictCursor,
            )
        except psycopg.OperationalError:
            raise Exception(
                f"Couldn't connect to the database {self._database_name()}! "
                f"Did you create it using `createdb {self._database_name()}`?"
            )

    # This method seeds the database with the given SQL file.
    def seed(self, sql_filename):
        self._check_connection()
        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does not exist")
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_filename, "r").read())
            self.connection.commit()

    # This method executes an SQL query on the database.
    def execute(self, query, params=[]):
        self._check_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description is not None:
                result = cursor.fetchall()
            else:
                result = None
            self.connection.commit()
            return result

    CONNECTION_MESSAGE = (
        ""
        "DatabaseConnection.exec_params: Cannot run a SQL query as "
        "the connection to the database was never opened. Did you "
        "make sure to call first the method DatabaseConnection.connect` "
        "in your app.py file (or in your tests)?"
    )

    # This private method checks that we're connected to the database.
    def _check_connection(self):
        if self.connection is None:
            raise Exception(self.CONNECTION_MESSAGE)

    # # This private method returns the name of the database we should use.
    def _database_name(self):
        if self.test_mode:
            return self.TEST_DATABASE_NAME
        else:
            return self.DEV_DATABASE_NAME
