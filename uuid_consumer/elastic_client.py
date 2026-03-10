from elasticsearch import Elasticsearch
from config import Config


logger = Config.logger


class ElasticClient:
    def __init__(self):
        self.elastic_client = Elasticsearch(Config.elastic_url)
        self.index = Config.elastic_index

        if not self.elastic_client.indices.exists(index=self.index):
            self.elastic_client.indices.create(index=self.index, body=Config.mapping)

    def insert_file(self, file_id, metadata):
        metadata['bds_is'] = False
        metadata['level_threat_bds'] = 'none'
        metadata['percent_bds'] = 0
        metadata['text'] = ''

        response = self.elastic_client.update(
            index=self.index,
            id=file_id,
            doc=metadata,
            doc_as_upsert=True
        )
        logger.info(f'file with id {file_id} inserted to elastic search.')
        logger.info(response.body)
        return response


