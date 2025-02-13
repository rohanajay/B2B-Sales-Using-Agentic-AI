# src/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API Key from environment variables
PREDICTIONGUARD_API_KEY = os.getenv("PREDICTIONGUARD_API_KEY")

# Output directory for generated quotes
OUTPUT_DIR = "output/generated_quotes"