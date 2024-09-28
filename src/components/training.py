from src.data_types import TrainingConfig
import tensorflow as tf


class Train:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def data_generator(self):
        if self.config.params_augmentation:
            train_generator = tf.keras.preprocessing.image.ImageDataGenerator(
                rescale = 1/255.,
                validation_split = 0.27,
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2
            )
        else:
            train_generator = tf.keras.preprocessing.image.ImageDataGenerator(
                rescale = 1/255.,
                validation_split = 0.27
            )
        self.train_generator = train_generator.flow_from_directory(
            directory = self.config.training_data,
            subset = 'training',
            shuffle = True,
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size
        )

        val_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale = 1/255.,
            validation_split = 0.27
        )
        self.val_generator = val_generator.flow_from_directory(
            directory = self.config.training_data,
            subset = 'validation',
            shuffle = True,
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size
        )

    def fit(self, callbacks: list):
        model = tf.keras.models.load_model(self.config.updated_model_path)
        steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        val_steps = self.val_generator.samples // self.val_generator.batch_size

        model.fit(
            self.train_generator,
            epochs = self.config.params_epochs,
            steps_per_epoch = steps_per_epoch,
            validation_data = self.val_generator,
            validation_steps = val_steps,
            callbacks = callbacks
        )

        model.save(self.config.trained_model_path)