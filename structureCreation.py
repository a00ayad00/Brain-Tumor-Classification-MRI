import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

basic_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils.py",
    "src/config.py",
    "src/pipeline/__init__.py",
    "src/data_types.py",
    "src/constants/__init__.py",
    "config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "notebooks/trials.ipynb",
    "templates/index.html"
]


for filepath in basic_files:
    filepath = Path(filepath)  # To make the path compatible with OS to avoid any error.
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Directory "{filedir}" for the file "{filename}" was created successfully...')

    if not os.path.exists(filepath):
        with open(filepath, 'w'):
            logging.info(f'File "{filename}" was created successfully...')
    else:
        logging.info(f'File "{filename}" already exists')