import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("PREDICTIONGUARD_API_KEY")

if api_key:
    print("API Key Loaded Successfully")
else:
    print("API Key Not Found")