import tensorflow as tf
from src.data_types import ModelConfig


class Model:
    def __init__(self, config: ModelConfig):
        self.config = config

    
    def download(self):
        self.model = tf.keras.applications.vgg19.VGG19(
            input_shape = self.config.params_image_size,
            include_top = self.config.params_include_top,
            weights = self.config.params_weights
        )
        self.model.save(self.config.config_model_path)

    
    @staticmethod
    def _prepare(model, freeze_all=True, freeze_till=None, learning_rate=0.01, classes=4):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        flatten = tf.keras.layers.Flatten()(model.output)
        output_dense = tf.keras.layers.Dense(classes, activation='softmax')(flatten)
        final_model = tf.keras.models.Model(
            inputs=model.input, outputs=output_dense
        )

        final_model.compile(
            optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss = tf.keras.losses.CategoricalCrossentropy(),
            metrics = ["accuracy"]
        )
        final_model.summary()

        return final_model


    def update(self):
        self.final_model = self._prepare(
            model = self.model,
            freeze_all = False,
            freeze_till = None,
            learning_rate = self.config.params_lr,
            classes = self.config.params_classes
        )
        self.final_model.save(self.config.config_updated_model_path)