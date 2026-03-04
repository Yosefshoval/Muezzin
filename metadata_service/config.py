import os
from logger.logger import Logger

class Config:
    audio_files_folder = os.getenv('podcasts_folder')

    kafka_topic = os.getenv('KAFKA_TOPIC')
    producer_config = {
        'bootstrap.servers' : os.getenv('KAFKA_URL')
    }

    elastic_host = os.getenv('ELASTIC_URL')

    my_logger = Logger.get_logger(name=' metadata extractor ', es_host=elastic_host)
    my_logger.info('logger created')