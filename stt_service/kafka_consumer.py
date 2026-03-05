from confluent_kafka import Consumer
from config import Config

logger = Config.logger

consumer = Consumer(Config.consumer_config)
consumer.subscribe([Config.kafka_topic])
logger.info(f'consumer created: {consumer.consumer_group_metadata()}')

def get_message():
    message = consumer.poll(1.0)
    logger.info('get_message.......')
    if not message:
        return None
    if message.error():
        logger.error(message.error())
    logger.info('get_message: True')
    return json.loads(message.value().decode())
