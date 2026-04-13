import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration settings
API_KEY = os.getenv('API_KEY')

# Add other configuration settings as needed
