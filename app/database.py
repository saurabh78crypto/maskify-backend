import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

# Load environment variables from .env
load_dotenv()

# MongoDB connection URL
MONGO_URL = os.getenv('MONGO_URL') 
DATABASE_NAME = "maskify"

try:
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DATABASE_NAME]
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to connect to MongoDB: {str(e)}")
