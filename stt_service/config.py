from os import getenv
import logging


class Config:
    audio_files_folder = os.getenv('podcasts_folder')

    producer_config = {}

    logger = logging.getLogger('metadata extractor')
    logging.basicConfig(level=logging.INFO)

