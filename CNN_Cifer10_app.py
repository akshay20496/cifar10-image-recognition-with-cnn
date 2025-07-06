import cv2
import numpy as np
from PIL import Image
import streamlit as st
from tensorflow.keras.models import load_model

# Load model
loaded_model = load_model('CNN_cifer10.keras')

st.title("🐶🛩️ CIFAR-10 Object Recognition with Convolutional Neural Network")

# Upload image file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img = np.array(img)

    resized_img = cv2.resize(img, (32,32), interpolation=cv2.INTER_CUBIC)
    resized_img = resized_img / 255.0
    resized_img = resized_img.reshape(1,32,32,3)

    class_names = ['airplane','automobile','bird','cat','deer',
                   'dog','frog','horse','ship','truck']

    prediction = loaded_model.predict(resized_img)
    predicted_class = class_names[np.argmax(prediction)]

    st.success(f"🧾 Predicted Class: **{predicted_class}**")
else:
    st.warning("📁 Please upload an image to get a prediction.")