from tensorflow.keras.models import load_model
from utils import preprocess_image
import numpy as np

# Load model once
model = load_model('model/pollen_model.h5')  # Adjust the path if needed
class_names = ['Alnus', 'Anomalous', 'Cupressaceae', 'Debris']
  # Update with your actual class names

def predict_pollen(image_path):
    img = preprocess_image(image_path)
    predictions = model.predict(img)
    index = np.argmax(predictions)
    confidence = predictions[0][index]
    return class_names[index], confidence
