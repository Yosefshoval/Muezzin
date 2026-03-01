from config import Config
from metadata_extractor import get_metadata
from kafka_producer import publish_message

logger = Config.logger


def get_metadata_for_files(folder_path: Path):
    logger.info('loop starting...')
    for file_path in folder_path.glob("**/*"):
        try:
            file_metadata = get_metadata(file_path)
            published = publish_message(file_metadata)
            logger.info(f'message pushed: {published}')

        except Exception as e:
            logger.error(f'{type(e)}: {e}')


if __name__ == "__main__":
    get_metadata_for_files(Config.audio_files_folder)