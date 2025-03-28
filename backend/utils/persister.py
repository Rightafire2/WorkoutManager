import pandas as pd
from backend.utils.logger import Logger
from backend.utils.client.db import DatabaseConnector
import json


class Persister:
    def __init__(self):
        self.logger = Logger(__name__, self.__class__.__name__)
        self.db = DatabaseConnector()

    def persist_workouts(self, data):
        """
        Persist data to the database.
        :param data: The data to persist, typically a list of dictionaries or a DataFrame
        """
        if data.empty:
            self.logger.logWarn("No data to persist.")
            return

        query = """
            INSERT INTO workout_gw.workouts (
                id, title, description, start_time, end_time, updated_at, created_at, exercises
            ) VALUES (
                :id, :title, :description, :start_time, :end_time, :updated_at, :created_at, :exercises
            ) ON CONFLICT (id) DO NOTHING;
        """

        try:
            for _, record in data.iterrows():
                record_dict = {
                    "id": record["workouts.id"],
                    "title": record["workouts.title"],
                    "description": record["workouts.description"],
                    "start_time": pd.to_datetime(record["workouts.start_time"]),
                    "end_time": pd.to_datetime(record["workouts.end_time"]),
                    "updated_at": pd.to_datetime(record["workouts.updated_at"]),
                    "created_at": pd.to_datetime(record["workouts.created_at"]),
                    "exercises": json.dumps(record["workouts.exercises"])
                }
                self.logger.logDebug(f"Executing SQL: {query} with values: {record_dict}")
                self.db.connect()
                self.db.execute_sql_query((query, record_dict))

            self.logger.logInfo("Data persisted successfully.")
        except Exception as e:
            self.logger.logError(f"Error persisting data: {e}")
