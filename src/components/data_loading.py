import os
from pathlib import Path
from src import logger
from src.utils import get_size
from src.data_types import DataConfig
import kaggle
import warnings


warnings.filterwarnings('ignore')
kaggle.api.authenticate()


class Data:
    def __init__(self, data_config: DataConfig):
        self.data_config = data_config

    def download(self):

        new_folder_name = self.data_config.data_folder_name
        artifacts_folder = self.data_config.artifacts_folder
        data_path = f'{artifacts_folder}/{new_folder_name}'

        if (not os.path.exists(Path(data_path+'/Training'))) or (get_size(data_path) > 0):
            kaggle.api.dataset_download_files(
                self.data_config.dataset_name,
                path=Path(data_path), unzip=True
            )

            logger.info(
                f'Data was downloaded successfully and saved at "{data_path}", with size ~{get_size(data_path)} MB'
            )
        else:
            logger.info(
                f'Data already exists and saved at "{data_path}", with size {get_size(data_path)}'
            )