from src.constants import CONFIG_PATH, PARAMS_PATH
from src.utils import read_yaml, create_dirs
from src.data_types import DataConfig


class ConfigManager:
    def __init__(self, config_path=CONFIG_PATH, params_path=PARAMS_PATH):
        self.config = read_yaml(CONFIG_PATH)
        self.params = read_yaml(PARAMS_PATH)

        create_dirs([self.config.artifacts_root])

    def get_data_config(self):
        data_config = self.config.data_ingestion
        return DataConfig(
            dataset_name=data_config.dataset_name,
            data_folder_name=data_config.data_folder_name,
            artifacts_root=self.config.artifacts_root
        )