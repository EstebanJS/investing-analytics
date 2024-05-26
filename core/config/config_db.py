import os

class ConfigDB:
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/mydatabase')
