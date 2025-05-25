from flask import Flask, render_template, request
import numpy as np
from keras.models import load_model
from PIL import Image, ImageChops, ImageEnhance
import os

app = Flask(__name__)
model = load_model('model/image_forgery_detection_casia2.h5')
class_labels = ['Fake', 'Real']
image_size = (128, 128)

def convert_to_ela_image(path, quality):
    temp_filename = 'temp_file_name.jpg'
    image = Image.open(path).convert('RGB')
    image.save(temp_filename, 'JPEG', quality=quality)
    temp_image = Image.open(temp_filename)
    ela_image = ImageChops.difference(image, temp_image)
    extrema = ela_image.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
    return ela_image

def prepare_image(image_path):
    return np.array(convert_to_ela_image(image_path, 90).resize(image_size)).flatten() / 255.0

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    filepath = os.path.join('static/uploads', file.filename)
    file.save(filepath)
    input_image = prepare_image(filepath)
    input_image = input_image.reshape(1, 128, 128, 3)
    prediction = model.predict(input_image)
    predicted_class = np.argmax(prediction, axis=1)[0]
    confidence = prediction[0][predicted_class] * 100
    # Pass prediction and confidence separately
    return render_template(
        'result.html',
        prediction=class_labels[predicted_class],
        confidence=f"{confidence:.2f}",
        image_filename=file.filename
    )

if __name__ == '__main__':
    app.run(debug=True)