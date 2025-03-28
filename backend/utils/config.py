from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
# DEBUG = os.getenv("DEBUG") == "True"
# TIMEOUT = int(os.getenv("TIMEOUT", 5))  # with default fallback
