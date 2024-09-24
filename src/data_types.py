from dataclasses import dataclass


@dataclass
class DataConfig:
    dataset_name: str
    data_folder_name: str
    artifacts_root: str