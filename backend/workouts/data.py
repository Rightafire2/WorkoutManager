from backend.utils.client.hevyapi import HevyAPI
import json
import pandas as pd
from backend.utils.client.db import DatabaseConnector
from backend.utils.persister import Persister
from backend.utils.logger import Logger


class WorkoutData:
    def __init__(self):
        self.api = HevyAPI()
        self.logger = Logger(__name__, self.__class__.__name__)

    def fetch_workouts(self):
        try:
            workouts = self.api.get_workouts()
            return workouts
        except Exception as e:
            self.logger.logError(f"Error fetching workouts: {e}")
            return None

    def convert_to_dataframe(self):
        # Fetch workouts from the API
        workouts = self.fetch_workouts()

        if not workouts:
            return pd.DataFrame()
        # Convert the workouts to a DataFrame
        try:
            # Assuming workouts is a list of dictionaries
            df = pd.DataFrame(workouts)
            flattened_df = pd.json_normalize(df.to_dict(orient='records'))
            return flattened_df.convert_dtypes()
        except Exception as e:
            self.logger.logError(f"Error converting workouts to DataFrame: {e}")
            return pd.DataFrame()

workout_data = WorkoutData()
df = workout_data.convert_to_dataframe()
persister = Persister()
persister.persist_workouts(df)
print(df["workouts.exercises"])