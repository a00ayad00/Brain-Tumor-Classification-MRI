from src.config import ConfigManager
from src.components.callbacks import Callbacks
from src.components.training import Train
from src import logger
import os


artifacts_folder = ConfigManager().artifacts_folder
config = ConfigManager().config

model_path = os.path.join(
    artifacts_folder, config.model.updated_model_path
)
trained_model_path = os.path.join(
    artifacts_folder, config.training.trained_model_path
)


step = "Step_3: Train the Model"


class train:
    def main():
        callbacks_config = ConfigManager().get_callbacks_config()
        callbacks = Callbacks(callbacks_config).get_callbacks()

        training_config = ConfigManager().get_training_config()
        train = Train(training_config)
        train.data_generator()
        train.fit(callbacks)


if __name__ == '__main__':
    try:
        logger.info(f"\n>>>>>>>  {step} has started to train the '{model_path}'...  <<<<<<<")
        train.main()
        logger.info(f"<<<<<<<  The model was trained successfully and saved at '{trained_model_path}' >>>>>>>\n")
    except Exception as e:
        logger.exception(e)
        raise e