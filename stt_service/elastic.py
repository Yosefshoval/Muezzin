from elasticsearch import Elasticsearch
from config import Config

logger = Config.logger

es = Elasticsearch(Config.elastic_url)
logger.info(f'Elastic client created and connected: {es.ping()}')


def update_file_metadata(file_id: str, text: str):
    file_data = es.search(index=Config.elastic_index, query={ "query" : { "term" : { "file_id": file_id } } } )
    file_data['text'] = text
    response = es.update(
        index=Config.elastic_index,
        id=file_id,
        doc=new_metadata
    )

    logger.info(f'file with id {file_id} inserted to elastic search.')
    logger.info(response.body)
    return response