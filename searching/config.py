import os
from logger.logger import Logger

class SearchingConfig:
    elastic_url = os.getenv('ELASTIC_URL')
    elastic_index = os.getenv('ELASTIC_INDEX')

    logger = Logger.get_logger(name='searching service', es_host=elastic_url)
    logger.info('logger created')
