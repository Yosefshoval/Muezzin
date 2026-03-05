import os
from logger.logger import Logger

class Config:
    elastic_url = os.getenv('ELASTIC_URL')
    elastic_index = os.getenv('ELASTIC_INDEX')

