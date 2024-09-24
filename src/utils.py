from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from src import logger
from ensure import ensure_annotations
from pathlib import Path
import os


@ensure_annotations  # See trials.ipynb from notebooks to see an example
def read_yaml(yaml_path: Path) -> ConfigBox:
    try:
        with open(yaml_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"The file: {yaml_path} loaded successfully...")
            return ConfigBox(content)  # See trials.ipynb from notebooks to see an example
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_dirs(dirs: list, verbose=True):
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)
        if verbose:
            logger.info(f"Directory '{dir}' was successfully created...")


@ensure_annotations
def get_size(path):
    if os.path.isfile(path):
        size = os.path.getsize(path)
    else:
        size = 0
        for path, dirs, files in os.walk(path):
            for f in files:
                fp = os.path.join(path, f)
                size += os.path.getsize(fp)

    return f"~ {round(size/(1024*1024), 2)} MB"

