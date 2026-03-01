import os
from os import getenv
import logging


class Config:
    audio_files_folder = os.getenv('podcasts_folder')

    kafka_topic = os.getenv('KAFKA_TOPIC')
    producer_config = {
        'bootstrap.servers' : os.getenv('KAFKA_URL')
    }

    logger = logging.getLogger('metadata extractor')
    logging.basicConfig(level=logging.INFO)