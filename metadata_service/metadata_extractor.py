from pathlib import Path
import datetime
from config import Config

logger = Config.logger


def get_metadata(file : Path):
    logger.info(f'getting_metadata for file: {file}')
    return {
        'file_name' : file.name,
        'created_at' : str(datetime.datetime.fromtimestamp(file.stat().st_ctime)),
        'modified_at' : str(datetime.datetime.fromtimestamp(file.stat().st_mtime)),
        'size' : file.stat().st_size,
        'suffix' : file.suffix
    }
