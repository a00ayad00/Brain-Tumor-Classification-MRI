from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np


class Inference:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def predict(self, file_path):
        idx_to_label = {
            0: 'Glioma Tumor',
            1: 'Meningioma Tumor',
            2: 'No Tumor',
            3: 'Pituitary Tumor'
        }

        img = image.load_img(file_path, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)

        scores = self.model.predict(img)[0]
        idx = np.argmax(scores, axis=0)

        return [{
            'Class': idx_to_label[idx],
            'Confidence': str(scores[idx])
        }]