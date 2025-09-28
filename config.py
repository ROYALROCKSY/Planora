import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "planora_db")
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-later")

# URL-encode password to handle special characters in password
ENCODED_PASSWORD = quote_plus(DB_PASSWORD)

# Build MongoDB URI
MONGO_URI = f"mongodb+srv://{DB_USER}:{ENCODED_PASSWORD}@cluster0.xmd6o1c.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
