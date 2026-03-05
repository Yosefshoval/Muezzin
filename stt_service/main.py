from config import Config
from elastic import update_file_metadata
from stt import extract_text
from pathlib import Path

logger = Config.logger

def get_binary_file(file: str):
    with open(file, "rb") as f:
        binary_file = f.read()
        logger.info(f'get file {file} in binary format.')
    return binary_file



def main(folder_path: Path):

    for file in folder_path.glob("**/*"):
        try:
            text = extract_text(str(file))

            file_id = hash(get_binary_file(str(file)))

            logger.info(f'file path: {file}. file id: {file_id}')
            updated_status = update_file_metadata(f'{file_id}', text)

            logger.info(f'file {file} handled successfully')
            logger.info(f'updated status: {updated_status}')
        except Exception as e:
            logger.error(e)


if __name__ == "__main__":
    main(Path(Config.audio_folder_path))