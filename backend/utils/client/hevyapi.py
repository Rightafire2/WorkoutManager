import requests
from backend.utils.config import API_URL, API_KEY

class HevyAPI:

    def __init__(self):
        self.api_key =API_KEY
        self.base_url = API_URL

    def get_workouts(self):
        url = f"{self.base_url}/workouts"
        headers = {
            "api-key": f"{self.api_key}",
            "accept": "application/json"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch workouts: {response.status_code} - {response.text}")

# if __name__ == "__main__":
#     api = HevyAPI()
#     try:
#         workouts = api.get_workouts()
#         print(json.dumps(workouts, indent=2))
#     except Exception as e:
#         print(e)