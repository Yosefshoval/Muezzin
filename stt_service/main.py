from config import Config
from elastic import update_file_metadata
from kafka_consumer import get_message
from stt import extract_text
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
            file_id = message['file_id']

            logger.info(f'file path: {message["file_path"]}. file id: {file_id}')

            updated_status = update_file_metadata(f'{file_id}', text)
            logger.info(f'updated status: {updated_status["result"]}')
            logger.info(f'file {message["file_path"]} handled successfully')

        except Exception as e:
            logger.error(f'{type(e)}: {e}')



if __name__ == "__main__":
    main()