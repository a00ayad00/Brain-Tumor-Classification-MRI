from src.constants import CONFIG_PATH, PARAMS_PATH
from src.utils import read_yaml, create_dirs
from src.data_types import DataConfig, ModelConfig, CallbacksConfig, TrainingConfig
from pathlib import Path
import os


class ConfigManager:
    def __init__(self, config_path=CONFIG_PATH, params_path=PARAMS_PATH):
        self.config = read_yaml(CONFIG_PATH)
        self.params = read_yaml(PARAMS_PATH)
        self.artifacts_folder = self.config.artifacts_root

        create_dirs([self.artifacts_folder])

    def get_data_config(self):
        data_config = self.config.data_ingestion
        return DataConfig(
            dataset_name=data_config.dataset_name,
            data_folder_name=data_config.data_folder_name,
            artifacts_root=self.artifacts_folder
        )

    def get_model_config(self):
        model_config = self.config.model
        model_params = self.params
        return ModelConfig(
            config_root_dir = Path(os.path.join(self.artifacts_folder, model_config.model_folder_name)),
            config_model_path = Path(os.path.join(self.artifacts_folder, model_config.model_path)),
            config_updated_model_path = Path(os.path.join(self.artifacts_folder, model_config.updated_model_path)),
            params_image_size = model_params.IMAGE_SIZE,
            params_lr = model_params.LEARNING_RATE,
            params_include_top = model_params.INCLUDE_TOP,
            params_weights = model_params.WEIGHTS,
            params_classes = model_params.CLASSES
        )

    def get_callbacks_config(self):
        config = self.config.callbacks
        tensorboard_dir = os.path.join(
            self.artifacts_folder, config.folder_name, config.tensorboard_folder_name
        )
        checkpoint_path = os.path.join(
            self.artifacts_folder, config.folder_name, config.checkpoint
        )
        
        create_dirs([
            tensorboard_dir,
            os.path.dirname(checkpoint_path)
        ])

        return CallbacksConfig(
            callbacks_folder = self.config.callbacks,
            tensorboard_dir = tensorboard_dir,
            checkpoint_path = checkpoint_path
        )

    def get_training_config(self):
        training_config = self.config.training
        training_data_path = os.path.join(
            self.artifacts_folder, self.config.data_ingestion.data_folder_name, 'Training'
        )

        return TrainingConfig(
            training_folder = os.path.join(self.artifacts_folder, training_config.folder_name),
            trained_model_path = os.path.join(self.artifacts_folder, training_config.trained_model_path),
            updated_model_path = os.path.join(self.artifacts_folder, self.config.model.updated_model_path),
            training_data = training_data_path,
            params_epochs = self.params.EPOCHS,
            params_batch_size = self.params.BATCH_SIZE,
            params_augmentation = self.params.AUGMENTATION,
            params_image_size = self.params.IMAGE_SIZE
        )