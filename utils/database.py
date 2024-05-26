from pymongo import MongoClient
from core.config import ConfigDB

class Database:
    def __init__(self):
        self.client = MongoClient(ConfigDB.MONGODB_URI)
        self.db = self.client.get_database()

    def get_collection(self, name):
        return self.db.get_collection(name)

db_instance = Database()
