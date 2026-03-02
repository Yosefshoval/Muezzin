from config import Config
from kafka_consumer import get_message
from elastic_client import ElasticClient
from mongo_client import MongoDB
from uuid import uuid4

logger = Config.logger
es = ElasticClient()
mongodb = MongoDB()


def main():
    logger.info('loop starting...')
    while True:
        try:
            message = get_message()
            if message is None:
                continue
            logger.info('message received')

            file_id = str(uuid4())
            inserted_to_es = es.insert_file(file_id, message)
            inserted_to_mongo = mongodb.insert_file()

        except Exception as e:
            logger.error(f'{type(e)}: {e}')
