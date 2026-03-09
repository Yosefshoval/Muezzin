from elastic import Elastic


def result_handler(result: dict):
    clean_result = []
    if result is not None:
        for item in result:
            if item['_source'].get('text'): item['_source']['text'] = f'{item["_source"]["text"][:100]}...'
            clean_result.append(item['_source'])
        return clean_result
    return result


def get_all(client: Elastic):
    query = { "query" : { "match_all" : { } } }
    result = client.exec_query(query)
    return result_handler(result)



def top_5_terrorists(client: Elastic):
    query = {
        "sort" : [
            {
                "percent_bds": {
                    "order": "desc"
                }
            }
        ],
        "size": 5,
        "query" : {
            "match_all" : {}
        }
    }

    result = client.exec_query(query)
    return result_handler(result)


def avg_precent_bds(client: Elastic):
    query = {
        "size": 0,
        "aggs": {
            "avg_precent_risk": {
                "avg": {"field": "percent_bds"}
            }
        }
    }
    result = client.exec_query(query, agg=True)
    return result

# query_structure = {
#     "from" : 0,
#     "size" : 10,
#     "_source" : ["id", "title", "status", "_created_at"],
#     "query" : {
#         "bool" : {
#             "must" : [
#                 { "exists" : { "field" : "known_associated" } },
#                 {"terms" : {"treat_level" : ["medium", "none"]}}
#             ],
#             "filter" : [
#                 {"term": {"activate" : True}}
#             ],
#             "must_not" : [
#                 {"term" : {"treat_level" : "HIGH"}}
#             ],
#             "should" : [
#                 {
#                 "nested" : {
#                                 "path" : "equipment",
#                                 "query" : {
#                                     "bool" : {
#                                         "filter" : [
#                                             {"term" : {"equipment.category" : "comms"}},
#                                             {"term" : {"equipment.category" : "good"}}
#                                         ]
#                                     }
#                                 }
#                             }
#                 }
#             ]
#         }
#     },
#     "sort": [],
#     "aggs": {},
#     "highlight": {}
# }