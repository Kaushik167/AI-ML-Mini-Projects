# 📸 Camera Classifier in Python

A Python project that builds a **real-time camera classifier** using computer vision and machine learning.  
This project was created by following an online YouTube tutorial to improve my understanding of Python, OpenCV, and machine learning concepts.

---

## 🎯 What Is This Project About?

This project uses a webcam to capture images, trains a machine learning model, and performs **live classification** on the camera feed.  
It demonstrates how Python can be used to combine **computer vision**, **machine learning**, and a **graphical user interface** into a single interactive application.

The classifier can be trained with custom image data and then used to predict classes in real time.

---

## ⚙️ How Does It Work?

1. **Webcam Access**  
   - The program accesses the webcam using OpenCV.
   - Images are captured and stored as training data.

2. **Image Processing**  
   - Captured images are resized and converted into a format suitable for machine learning.

3. **Model Training**  
   - A Support Vector Machine (SVM) classifier is trained using `scikit-learn`.

4. **Real-Time Prediction**  
   - Live frames from the webcam are passed to the trained model.
   - Predictions are displayed instantly.

5. **Graphical User Interface**  
   - A Tkinter-based GUI allows users to capture images, train the model, and view predictions easily.

---

## 🛠 Technologies & Libraries Used

- Python 3  
- OpenCV (`cv2`) – webcam capture and image processing  
- scikit-learn – machine learning (SVM classifier)  
- Tkinter – graphical user interface  
- Pillow (PIL) – image handling  

---

## 📚 Things Learned

- Capturing live video using OpenCV  
- Image preprocessing for machine learning  
- Training and using an SVM classifier  
- Integrating machine learning with a GUI  
- Building interactive Python applications  
- Understanding real-time prediction workflows  

---

## 🧾 Credits

- 📹 **Video Credits:** [Building A Camera Classifier in Python by NeuralNine](https://www.youtube.com/watch?v=CeTR_-ALdRw)
- 🤖 **README file:** Done with the help of ChatGPT  

---
