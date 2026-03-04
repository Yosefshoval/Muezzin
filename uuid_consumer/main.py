from config import Config
from kafka_consumer import get_message
from elastic_client import ElasticClient
from mongo_client import MongoDB
from uuid import uuid4

logger = Config.logger
es = ElasticClient()
mongodb = MongoDB()



def get_binary_file(file_path: str) -> bytes | None:
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            logger.info(f'read file {file_path} in binary format')
        return content
    except Exception as e:
        logger.error(e)



def main():
    logger.info('loop starting...')
    while True:
        try:
            message = get_message()
            if message is None:
                continue

            message['file_id'] = str(uuid4())
            logger.info(f'message received. new id: {message['file_id']}')
            es.insert_file(message['file_id'], message)
            binary_file = get_binary_file(message['file_path'])
            mongodb.insert_file(binary_file, message)

        except Exception as e:
            logger.error(f'{type(e)}: {e}')


if __name__ == "__main__":
    main()