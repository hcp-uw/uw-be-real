import os
from dotenv import load_dotenv

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# load secrets
mongo_env_path = os.path.join(os.getcwd(), "secrets", "mongodb", ".env")
load_dotenv(mongo_env_path)

uri = os.getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
