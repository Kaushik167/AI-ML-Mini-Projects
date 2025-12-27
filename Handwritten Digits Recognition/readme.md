# ✏️ Handwritten Digit Recognition with Neural Networks

A machine learning project that builds a **neural network to recognize handwritten digits** using Python and TensorFlow, trained on the MNIST dataset.  
This project was created by following the YouTube tutorial *“Neural Network Python Project – Handwritten Digit Recognition”*.

---

## 🧠 Project Overview

The goal of this project is to create a neural network that can classify handwritten digits (0–9) with high accuracy.  
It uses the **MNIST dataset**, which contains thousands of images of handwritten digits, and trains a neural network model to learn and recognize them. :contentReference[oaicite:2]{index=2}

---

## ⚙️ How It Works

1. **Load the MNIST Dataset**  
   - The dataset contains 60,000 training images and 10,000 test images of handwritten digits. :contentReference[oaicite:3]{index=3}

2. **Preprocess Input Data**
   - Normalize pixel values from 0–255 to 0–1 to help the neural network learn more efficiently.

3. **Build the Neural Network**
   - Use TensorFlow/Keras to define a model with multiple layers.
   - Flatten the 28×28 images into vectors, then pass through dense layers.

4. **Train the Model**
   - Train for several epochs to reduce loss and increase accuracy.

5. **Evaluate & Predict**
   - Test the model on unseen test images and output classification accuracy.

---

## 🛠 Technologies & Libraries Used

- Python 3  
- **TensorFlow / Keras** — deep learning framework  
- NumPy — numerical operations  
- OpenCV (optional) — visualization  
- Matplotlib (optional) — image display

---

## 📚 Things Learned

- How to import and use the MNIST dataset  
- Normalizing image data for machine learning  
- Creating a neural network classifier with TensorFlow  
- Training and evaluating a model  
- Understanding loss, accuracy, and prediction  
- Using dense layers and activation functions

---

## 🧾 Credits

- 📹 **Video Credits:** [Neural Network Python Project - Handwritten Digit Recognition by NeuralNine](https://www.youtube.com/watch?v=bte8Er0QhDg)
- 🤖 **README file:** Done with the help of ChatGPT  

---
