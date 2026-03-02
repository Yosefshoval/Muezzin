from pymongo import MongoClient
from config import Config


logger = Config.logger

class MongoDB:
    def __init__(self):
        client = MongoClient
