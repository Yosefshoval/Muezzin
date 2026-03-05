import os
from logger.logger import Logger


class Config:
    kafka_url = os.getenv('KAFKA_URL')
    kafka_topic = os.getenv('KAFKA_TOPIC')
    kafka_produce_topic = os.getenv('KAFKA_PRODUCE_TOPIC')

    mongo_url = os.getenv('MONGO_URL')
    mongo_database = os.getenv('MONGO_DATABASE')

    elastic_url = os.getenv('ELASTIC_URL')
    elastic_index = os.getenv('ELASTIC_INDEX')

    consumer_config = {
        "bootstrap.servers" : kafka_url,
        "group.id" : "uuid_service",
        "auto.offset.reset" : "earliest"
    }

    producer_config = {
        "bootstrap.servers" : kafka_url
    }

    logger = Logger.get_logger(name=' uuid_service ', es_host=elastic_url)
