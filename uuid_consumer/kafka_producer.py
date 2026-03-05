from confluent_kafka import Producer
from config import Config
import json

logger = Config.logger

producer = Producer(Config.producer_config)

def callback(err, msg):
    if err:
        print(err)
        logger.error(err)
    else:
        print(f'message {msg.value()} pushed successfully to kafka on topic {Config.kafka_topic}')
        logger.info(f'message {msg.value()} pushed successfully to kafka on topic {Config.kafka_topic}')


def publish(message: dict):
    producer.produce(
        topic=Config.kafka_produce_topic,
        value=json.dumps(message).encode(),
        callback=callback
    )

    producer.flush()
