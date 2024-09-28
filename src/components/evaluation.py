import tensorflow as tf
import json
from src import logger
from src.data_types import EvalConfig
import warnings


warnings.filterwarnings('ignore')


class Eval:
    def __init__(self, config: EvalConfig):
        self.config = config

    def _data_generator(self):
        generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale = 1./255)
        self.generator = generator.flow_from_directory(
            directory = self.config.testing_data,
            shuffle = False,
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
        )

    def eval(self, path):
        model = tf.keras.models.load_model(self.config.model_path)
        self._data_generator()
        score = model.evaluate(self.generator)
        data = {
            'loss': score[0],
            'accuracy': score[1]
        }
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
            logger.info(f"\nEvaluation file saved at: {path}\n")