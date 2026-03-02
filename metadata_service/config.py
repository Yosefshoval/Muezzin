import os
from os import getenv
from logger import Logger


class Config:
    audio_files_folder = os.getenv('podcasts_folder')

    kafka_topic = os.getenv('KAFKA_TOPIC')
    producer_config = {
        'bootstrap.servers' : os.getenv('KAFKA_URL')
    }

    logger = Logger.get_logger(name=' metadata extractor ', es_host=Config.elastic_host)

    elastic_host = os.getenv('ELASTIC_URL')