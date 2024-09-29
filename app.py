from flask import Flask, request, jsonify, render_template
from src.utils import decode_img
from src.pipeline.inference import Inference
import os


model_path = os.path.join('artifacts', 'training', 'model.h5')
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def classify():
    img = request.json['image']
    decode_img(img, 'input_img.jpg')
    output = Inference(model_path).predict('input_img.jpg')
    return jsonify(output)


if __name__ == "__main__":
    app.run('0.0.0.0', port=8080, debug=True)