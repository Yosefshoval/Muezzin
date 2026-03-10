from pathlib import Path
import datetime
from config import Config

logger = Config.my_logger


def get_metadata(file : Path):
    logger.info(f'getting_metadata for file: {file}')
    metadata = {
        'file_name' : file.name,
        'created_at' : str(datetime.datetime.fromtimestamp(file.stat().st_ctime).strftime("%Y-%m-%d %H:%M:%S")),
        'modified_at' : str(datetime.datetime.fromtimestamp(file.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")),
        'size' : file.stat().st_size,
        'suffix' : file.suffix
    }
    logger.info(f'metadata: {metadata}')
    return metadata
