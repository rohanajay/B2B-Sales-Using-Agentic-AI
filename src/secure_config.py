import os
from dotenv import load_dotenv, set_key, find_dotenv
from getpass import getpass

# Define path to .env file
env_path = find_dotenv()
if not env_path:
    env_path = ".env"

# Load existing .env file
load_dotenv(env_path)

# Check if the API key already exists
if os.getenv("PREDICTIONGUARD_API_KEY"):
    print("API key already set in .env")
else:
    # Securely input API key
    api_key = getpass("Enter your Prediction Guard API Key: ")
    
    # Store it securely in .env
    set_key(env_path, "PREDICTIONGUARD_API_KEY", api_key)
    print("API key securely stored in .env")
