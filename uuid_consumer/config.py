import os
import logging
from logger import Logger

logger = Logger.get_logger()

class Config:
    kafka_url = os.getenv('KAFKA_URL')
    kafka_topic = os.getenv('KAFKA_TOPIC')

    mongo_url = os.getenv('MONGO_URL')
    mongo_user = os.getenv('MONGO_USER')
    mongo_password = os.getenv('MONGO_PASSWORD')

    elastic_url = os.getenv('ELASTIC_URL')
    elastic_index = os.getenv('ELASTIC_INDEX')

    consumer_config = {
        "bootstrap.servers" : kafka_url,
        "group.id" : "uuid_service",
        "auto.offset.reset" : "earliest"
    }

    logger = logging.getLogger(" uuid_generator ")
    logging.basicConfig(level=logging.INFO)