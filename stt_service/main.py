from config import Config
from elastic import update_file_metadata
from kafka_consumer import get_message
from stt import extract_text
from risk_calc import risk_rank, risk_percent
from pathlib import Path

logger = Config.logger

def get_binary_file(file: str):
    with open(file, "rb") as f:
        binary_file = f.read()
        logger.info(f'get file {file} in binary format.')
    return binary_file



def main():
    while True:
        try:
            message = get_message()
            if message is None:
                continue

            logger.info('message received')

            text = extract_text(message['file_path'])

            message['text'] = text
            message['percent_bds'] = risk_percent(text.lower())
            message['level_threat_bds'] = risk_rank(text.lower())
            message['bds_is'] = True if message['percent_bds'] > 30 else False

            file_id = message['file_id']

            logger.info(f'file path: {message["file_path"]}. file id: {file_id}')

            updated_status = update_file_metadata(f'{file_id}', message)
            logger.info(f'updated status: {updated_status["result"]}')
            logger.info(f'file {message["file_path"]} handled successfully')

        except Exception as e:
            logger.error(f'{type(e)}: {e}')



if __name__ == "__main__":
    main()