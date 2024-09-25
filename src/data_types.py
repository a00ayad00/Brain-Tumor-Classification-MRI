from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataConfig:
    dataset_name: str
    data_folder_name: str
    artifacts_root: str


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