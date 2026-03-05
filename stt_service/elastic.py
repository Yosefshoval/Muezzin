from elasticsearch import Elasticsearch
from config import Config

logger = Config.logger
es = Elasticsearch(Config.elastic_url)
logger.info(f'Elastic client created and connected: {es.ping()}')


def update_file_metadata(file_id: str, text: str):
    result = es.search(index=Config.elastic_index, query={ "match" : { "file_id" : file_id } } )
    logger.info(f'matches result for id {file_id}: {len(result['hits']['hits'])}')
    file_data = result['hits']['hits']
    if not file_data:
        logger.error(f'no such file with id {file_id}')
        return False

    new_metadata = file_data[0]['_source']
    new_metadata['text'] = text

    response = es.update(
        index=Config.elastic_index,
        id=file_id,
        doc=new_metadata,
        doc_as_upsert=True
    )

    logger.info(f'file with id {file_id} inserted to elastic search.')
    logger.info(response.body)
    return response

