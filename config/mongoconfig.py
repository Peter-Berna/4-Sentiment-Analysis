from pymongo import MongoClient
import dotenv
import os

dotenv.load_dotenv

dburl = "mongodb://localhost:27017"

if not dburl:
    raise ValueError("No URL for database")

client = MongoClient()
db = client.get_database("Ironhack")
c = db["HP"]