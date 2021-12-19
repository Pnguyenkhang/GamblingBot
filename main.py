from dotenv import load_dotenv
import os

load_dotenv()
# Environment variables

API_KEY = os.getenv("API_KEY")
print(API_KEY)