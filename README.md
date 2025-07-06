# cifar10-image-recognition-with-cnn
A Streamlit app to classify CIFAR-10 images using a CNN

# 🧠 CNN CIFAR-10 Classification App

This project contains a complete pipeline for classifying images from the **CIFAR-10** dataset using a **Convolutional Neural Network (CNN)** in TensorFlow, along with a **Streamlit web app** for easy user interaction.

---

## 🚀 Features

- 📊 Train a CNN on CIFAR-10 dataset using TensorFlow/Keras
- 💾 Save and load the trained model (`CNN_cifer10.keras`)
- 🌐 Streamlit web app to upload and classify new images
- 🖼️ Supports image display and predictions on user-uploaded data

---

## 🧱 Repository Structure

├── CNN_Cifer10_data.ipynb # Jupyter notebook for training CNN
├── CNN_Cifer10_app.py # Streamlit app for image prediction
├── CNN_cifer10.keras # Saved trained CNN model
├── requirements.txt # Required libraries
└── README.md # Project documentation

## 📁 Model

The trained model is saved as:

**CNN_cifer10.keras**

Loaded in the Streamlit app to classify user-uploaded CIFAR-10 style images.

## Classes

✈️ Airplane	
🚗 Automobile	
🐦 Bird	
🐱 Cat	
🦌 Deer	
🐶 Dog	
🐸 Frog	
🐴 Horse	
🚢 Ship	
🚚 Truck

## 📦 Requirements
Dependencies (also in requirements.txt):

pip install tensorflow
pip install opencv-python
pip install Pillow
pip install streamlit

## App output

![app_output](https://github.com/user-attachments/assets/6058d517-4fa8-4dcb-8832-3cb4c566698b)
