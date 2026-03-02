from pymongo import MongoClient
from config import Config
from gridfs import GridFS

logger = Config.logger

class MongoDB:
    def __init__(self):
        self.client = MongoClient(Config.mongo_url)

    def get_collection(self):
        db = self.client[Config.mongo_database]
        fs_coll = GridFS(db)
        return fs_coll


    def insert_file(self, binary_file: bytes, metadata: dict):
        coll = self.get_collection()
        inserted_result = coll.put(
            binary_file,
            file_name=metadata['file_name'],
            metadata=metadata
        )
        logger.info(f'file inserted to mongodb. result: {inserted_result}')
