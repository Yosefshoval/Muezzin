from config import Config
from kafka_consumer import get_message
from elastic import update_file_metadata
from stt import extract_text


logger = Config.logger

def main():
    while True:
        try:
            metadata = get_message()
            if not metadata:
                continue

            text = extract_text(metadata['file_path'])
            metadata['text'] = text
            updated_status = update_file_metadata(metadata['file_id'], metadata)
            logger.info(f'file {metadata["file_path"]} handled successfully')
            logger.info(f'updated status: {updated_status}')

        except Exception as e:
            logger.error(e)

if __name__ == "main":
    main()