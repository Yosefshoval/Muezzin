from elastic import Elastic

def top_5_terrorists(client: Elastic):
    query = {"match_all" : {}}
    result = client.exec_query(query)
    return result

