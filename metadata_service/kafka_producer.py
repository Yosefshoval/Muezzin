from confluent_kafka import Producer
import json
from config import Config

logger = Config.my_logger

logger.info('kafka producer file: ')
producer = Producer(Config.producer_config)
logger.info('Producer created')

def callback(err, msg):
    if err:
        print(err)
        logger.error(err)
    else:
        print(f'message {msg.value()} pushed successfully to kafka on topic {Config.kafka_topic}')
        logger.info(f'message {msg.value()} pushed successfully to kafka on topic {Config.kafka_topic}')


def publish_message(message: dict):
    value = json.dumps(message).encode()

    producer.produce(
        topic=Config.kafka_topic,
        value=value,
        callback=callback
    )
    producer.flush()