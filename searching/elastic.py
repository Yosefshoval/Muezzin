from elasticsearch import Elasticsearch
from config import SearchingConfig

class Elastic:
    def __init__(self):
        self.client = Elasticsearch(SearchingConfig.elastic_url)
        self.index = SearchingConfig.elastic_index
        SearchingConfig.logger.info(f'elasticsearch client created. {self.client.ping()}')


    def exec_query(self, query: dict):
        response = self.client.search(
            index=self.index,
            query=query
            )

        absolut_result = response['hits']['hits']
        SearchingConfig.logger.info(f'response from elastic query. matches: {len(absolut_result)}')
        if not absolut_result:
            return None
        return absolut_result