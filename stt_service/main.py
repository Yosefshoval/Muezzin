from config import Config
from elastic import update_file_metadata
from stt import extract_text
from pathlib import Path

logger = Config.logger

def get_binary_file(file: Path):
    with open(file, "rb") as f:
        binary_file = f.read()
    return binary_file



def main(folder_path: Path):

    for file in folder_path.glob("**/*"):
        try:
            text = extract_text(str(file))

            file_id = str(hash(get_binary_file(file)))
            updated_status = update_file_metadata(file_id, text)

            logger.info(f'file {file} handled successfully')
            logger.info(f'updated status: {updated_status}')
        except Exception as e:
            logger.error(e)


if __name__ == "main":
    main(Path(Config.audio_folder_path))