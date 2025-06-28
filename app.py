from flask import Flask, render_template, request
from classify import predict_pollen
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            image.save(path)
            label, confidence = predict_pollen(path)
            confidence *= 100
            return render_template('index.html', label=label, confidence=round(confidence, 2), image_path=path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
