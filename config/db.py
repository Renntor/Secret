import os

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.environ.get('MONGODB_URL')

conn = AsyncIOMotorClient(MONGODB_URL)