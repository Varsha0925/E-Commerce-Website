import tensorflow as tf
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np

def predict_object_from_request(file):
    # Load the MobileNet model with pre-trained weights
    model = MobileNet(weights='imagenet')

    # Load and preprocess the image
    img = Image.open(file.stream).convert('RGB')
    img = img.resize((224, 224))
    
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Make predictions
    predictions = model.predict(x)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # Print and return the top prediction
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        print(f"{i + 1}: {label} ({score:.2f})")

    top_prediction = decoded_predictions[0]
    return top_prediction[1]