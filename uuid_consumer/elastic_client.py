from elasticsearch import Elasticsearch
from config import Config


logger = Config.logger


class ElasticClient:
    def __init__(self):
        self.elastic_client = Elasticsearch(Config.elastic_url)
        self.index = Config.elastic_index
        self.elastic_client.create(
            index=self.index
        )

    def insert_file(self, file_id, metadata):
        response = self.elastic_client.update(
            index=self.index,
            id=file_id,
            doc=metadata
        )
        logger.info(f'file with id {file_id} inserted to elastic search.')
        logger.info(response.body)
        return response


