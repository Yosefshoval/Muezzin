import os
from logger.logger import Logger

class Config:
    elastic_url = os.getenv('ELASTIC_URL')
    elastic_index = os.getenv('ELASTIC_INDEX')

    kafka_url = os.getenv('KAFKA_URL')
    kafka_topic = os.getenv('KAFKA_TOPIC')

    consumer_config = {
        "bootstrap.servers" : kafka_url,
        "group.id" : "stt_service",
        "auto.offset.reset" : "earliest"
    }

    audio_folder_path = os.getenv('audio_folder_path')

    logger = Logger.get_logger(name=' stt_service ', es_host=elastic_url)
    logger.info('logger created')