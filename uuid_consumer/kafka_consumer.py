from config import Config
from confluent_kafka import Consumer
import json

logger = Config.logger

consumer = Consumer(Config.consumer_config)

def get_message():
    message = consumer.poll(1.0)
    if not message:
        return None
    if message.error():
        logger.error(message.error())
    return json.loads(message.value().decode())