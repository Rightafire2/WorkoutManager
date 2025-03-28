import pandas as pd
import sqlalchemy
import psycopg2  # Ensure psycopg2 is imported for PostgreSQL connection
from sqlalchemy import text
from sqlalchemy.engine import Engine
from backend.utils.config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE


class DatabaseConnector:
    """
    A class to handle database connections using SQLAlchemy
    """
    def __init__(self):
        self.db_user = DB_USER
        self.db_host = DB_HOST
        self.db_password = DB_PASSWORD
        self.db_port = DB_PORT
        self.db_database = DB_DATABASE
        self.db_url = f"postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_database}"
        self.engine: Engine = None

    def connect(self):
        try:
            self.engine = sqlalchemy.create_engine(self.db_url, connect_args={"password": self.db_password})
            # Test the connection
            with self.engine.connect() as connection:
                print("Connection to the database was successful.")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def execute_sql_query(self, query: str):
        """
        Execute a SQL query on the connected database.
        :param query: SQL query to execute
        :return: Result of the query execution
        """
        try:
            sql, params = query
            with self.engine.begin() as connection:
                connection.execute(text(sql), params)
        except Exception as e:
            print(f"Error executing query: {e}")
            return None