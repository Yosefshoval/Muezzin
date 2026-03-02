import os

class Config:
    kafka_url = os.getenv('KAFKA_URL')
    kafka_topic = os.getenv('KAFKA_TOPIC')

    mongo_url = os.getenv('MONGO_URL')
    mongo_user = os.getenv('MONGO_USER')
    mongo_password = os.getenv('MONGO_PASSWORD')

    elastic_url = os.getenv('ELASTIC_URL')

    consumer_config = {
        "bootstrap.servers" : kafka_url,
        "group.id" : "uuid_service",
        "auto.offset.reset" : "earliest"
    }