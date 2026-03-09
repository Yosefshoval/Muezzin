from elastic import Elastic


def result_handler(result: dict):
    clean_result = []
    if result is not None:
        for item in result:
            clean_result.append(item['_source'])
        return clean_result
    return result


def get_all(client: Elastic):
    query = { "query" : { "match_all" : { } } }
    result = client.exec_query(query)
    return result_handler(result)



def top_5_terrorists(client: Elastic):
    query = {}
    result = client.exec_query(query)
    return result_handler(result)
