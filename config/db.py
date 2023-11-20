import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.environ.get('MONGODB_URL')

client = MongoClient(MONGODB_URL)

db = client.secret_db

collection_name = db['secret_collection']
