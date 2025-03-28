from backend.utils.hevyapi import HevyAPI
import json
import pandas as pd

class WorkoutData:
    def __init__(self):
        self.api = HevyAPI()

    def fetch_workouts(self):
        try:
            workouts = self.api.get_workouts()
            return workouts
        except Exception as e:
            print(f"Error fetching workouts: {e}")
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
            flattened_df = pd.json_normalize(df.to_dict(orient='records'))  # Flatten nested dictionaries if any
            return flattened_df.columns
        except Exception as e:
            print(f"Error converting workouts to DataFrame: {e}")
            return pd.DataFrame()

workout_data = WorkoutData()
df = workout_data.convert_to_dataframe()
print(df)