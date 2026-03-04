from config import Config
from metadata_extractor import get_metadata
from kafka_producer import publish_message
from pathlib import Path

logger = Config.my_logger

def get_metadata_for_files(folder_path: Path):
    logger.info(f'loop starting. follow on folder: {folder_path}. folder exist: {folder_path.exists()}')
    for file_path in folder_path.glob("**/*"):
        try:
            logger.info(f'current file: {file_path}')
            file_metadata = get_metadata(file_path)
            file_metadata['file_path'] = str(file_path)
            published = publish_message(file_metadata)
            logger.info(f'message pushed: {published}')

        except Exception as e:
            logger.error(f'{type(e)}: {e}')


if __name__ == "__main__":
    get_metadata_for_files(Path(Config.audio_files_folder))