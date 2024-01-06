from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()
host = os.getenv("MONGO_URI")

try:
    connect(db="Countries", host=host)
except Exception as e:
    print(f"Error : {e}")
