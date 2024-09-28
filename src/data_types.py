from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataConfig:
    dataset_name: str
    data_folder_name: str
    artifacts_folder: str


@dataclass
class ModelConfig:
    config_root_dir: Path
    config_model_path: Path
    config_updated_model_path: Path
    params_image_size: list
    params_lr: float
    params_include_top: bool
    params_weights: str
    params_classes: int


@dataclass
class CallbacksConfig:
    callbacks_folder: str
    tensorboard_dir: str
    checkpoint_path: str


@dataclass
class TrainingConfig:
    training_folder: str
    trained_model_path: str
    updated_model_path: str
    training_data: str
    params_epochs: int
    params_batch_size: int
    params_augmentation: bool
    params_image_size: list


@dataclass
class EvalConfig:
    model_path: str
    testing_data: str
    params_image_size: list
    params_batch_size: int