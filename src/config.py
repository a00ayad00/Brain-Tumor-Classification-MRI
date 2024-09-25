from src.constants import CONFIG_PATH, PARAMS_PATH
from src.utils import read_yaml, create_dirs
from src.data_types import DataConfig, ModelConfig
from pathlib import Path
import os


class ConfigManager:
    def __init__(self, config_path=CONFIG_PATH, params_path=PARAMS_PATH):
        self.config = read_yaml(CONFIG_PATH)
        self.params = read_yaml(PARAMS_PATH)
        self.artifacts_root = self.config.artifacts_root

        create_dirs([self.config.artifacts_root])

    def get_data_config(self):
        data_config = self.config.data_ingestion
        return DataConfig(
            dataset_name=data_config.dataset_name,
            data_folder_name=data_config.data_folder_name,
            artifacts_root=self.config.artifacts_root
        )

    def get_model_config(self):
        model_config = self.config.model
        model_params = self.params
        return ModelConfig(
            config_root_dir = Path(os.path.join(self.artifacts_root, model_config.model_folder_name)),
            config_model_path = Path(os.path.join(self.artifacts_root, model_config.model_path)),
            config_updated_model_path = Path(os.path.join(self.artifacts_root, model_config.updated_model_path)),
            params_image_size = model_params.IMAGE_SIZE,
            params_lr = model_params.LEARNING_RATE,
            params_include_top = model_params.INCLUDE_TOP,
            params_weights = model_params.WEIGHTS,
            params_classes = model_params.CLASSES
        )