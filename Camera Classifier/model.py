import os
import numpy as np
import cv2 as cv
from PIL import Image
from sklearn.svm import LinearSVC

class Model:
    def __init__(self):
        self.model = LinearSVC()

    def train_model(self, counters):
        """
        Train the LinearSVC model using images stored in folders '1/' and '2/'.
        counters: list[int, int] containing the number of images captured per class +1
        """
        img_list = []
        class_list = []

        # Class 1 images
        for i in range(1, counters[0]):
            path = f'1/frame{i}.jpg'
            if not os.path.exists(path):
                continue
            img = cv.imread(path, cv.IMREAD_GRAYSCALE)
            if img is None:
                continue
            img_list.append(img.flatten())
            class_list.append(1)

        # Class 2 images
        for i in range(1, counters[1]):
            path = f'2/frame{i}.jpg'
            if not os.path.exists(path):
                continue
            img = cv.imread(path, cv.IMREAD_GRAYSCALE)
            if img is None:
                continue
            img_list.append(img.flatten())
            class_list.append(2)

        if len(img_list) == 0:
            raise ValueError("No images found! Capture at least 1 image per class before training.")

        # Convert to numpy arrays
        img_array = np.array(img_list)
        class_array = np.array(class_list)

        # Fit the SVM model
        self.model.fit(img_array, class_array)
        print("Model successfully trained!")

    def predict(self, frame_tuple):
        """
        Predict the class of a given frame.
        frame_tuple: (ret, frame) from Camera.get_frame()
        Returns: 1 or 2
        """
        ret, frame = frame_tuple
        if not ret or frame is None:
            return None

        # Convert to grayscale and resize using Pillow
        img = Image.fromarray(cv.cvtColor(frame, cv.COLOR_RGB2GRAY))
        img.thumbnail((150, 150), Image.Resampling.LANCZOS)

        # Flatten and predict
        img_array = np.array(img).flatten()
        prediction = self.model.predict([img_array])

        return prediction[0]
