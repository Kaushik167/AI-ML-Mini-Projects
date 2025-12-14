import tkinter as tk
from tkinter import simpledialog, messagebox
import cv2 as cv
import os
from PIL import Image, ImageTk
import model
import camera

class App:
    def __init__(self, window=tk.Tk(), window_title="Camera Classifier v0.1 Alpha"):
        self.window = window
        self.window_title = window_title

        self.counters = [1, 1]
        self.model = model.Model()
        self.auto_predict = False
        self.camera = camera.Camera()

        # Ask for class names first
        self.classname_one = simpledialog.askstring(
            "Classname One", "Enter the name of the first class:", parent=self.window
        )
        self.classname_two = simpledialog.askstring(
            "Classname Two", "Enter the name of the second class:", parent=self.window
        )

        self.init_gui()
        self.delay = 15
        self.update()

        self.window.attributes("-topmost", True)
        self.window.mainloop()

    def init_gui(self):
        self.canvas = tk.Canvas(self.window, width=self.camera.width, height=self.camera.height)
        self.canvas.pack()

        self.btn_toggleauto = tk.Button(self.window, text="Auto Prediction", width=50, command=self.auto_predict_toggle)
        self.btn_toggleauto.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_one = tk.Button(self.window, text=self.classname_one, width=50, command=lambda: self.save_for_class(1))
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_two = tk.Button(self.window, text=self.classname_two, width=50, command=lambda: self.save_for_class(2))
        self.btn_class_two.pack(anchor=tk.CENTER, expand=True)

        self.btn_train = tk.Button(self.window, text="Train Model", width=50, command=self.train_model)
        self.btn_train.pack(anchor=tk.CENTER, expand=True)

        self.btn_predict = tk.Button(self.window, text="Predict", width=50, command=self.predict)
        self.btn_predict.pack(anchor=tk.CENTER, expand=True)

        self.btn_reset = tk.Button(self.window, text="Reset", width=50, command=self.reset)
        self.btn_reset.pack(anchor=tk.CENTER, expand=True)

        self.class_label = tk.Label(self.window, text="CLASS")
        self.class_label.config(font=("Arial", 20))
        self.class_label.pack(anchor=tk.CENTER, expand=True)

    def auto_predict_toggle(self):
        if not self.is_model_trained():
            messagebox.showwarning("Model Not Trained", "Please train the model first!")
            return
        self.auto_predict = not self.auto_predict

    def save_for_class(self, class_num):
        ret, frame = self.camera.get_frame()
        if not ret:
            messagebox.showerror("Camera Error", "Cannot capture frame from camera.")
            return

        folder = str(class_num)
        if not os.path.exists(folder):
            os.mkdir(folder)

        file_path = f'{folder}/frame{self.counters[class_num-1]}.jpg'

        # Save grayscale image
        gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        cv.imwrite(file_path, gray)

        # Resize using Pillow
        img = Image.open(file_path)
        img.thumbnail((150, 150), Image.Resampling.LANCZOS)
        img.save(file_path)

        self.counters[class_num - 1] += 1

    def reset(self):
        for folder in ['1', '2']:
            if os.path.exists(folder):
                for file in os.listdir(folder):
                    file_path = os.path.join(folder, file)
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
        self.counters = [1, 1]
        self.model = model.Model()
        self.class_label.config(text="CLASS")
        self.auto_predict = False

    def train_model(self):
        try:
            self.model.train_model(self.counters)
            messagebox.showinfo("Training", "Model successfully trained!")
        except ValueError as e:
            messagebox.showerror("Training Error", str(e))

    def is_model_trained(self):
        # LinearSVC sets coef_ only after training
        return hasattr(self.model.model, "coef_")

    def update(self):
        if self.auto_predict:
            self.predict()

        ret, frame = self.camera.get_frame()
        if ret and frame is not None:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update)

    def predict(self):
        if not self.is_model_trained():
            messagebox.showwarning("Model Not Trained", "Please train the model first!")
            return None

        ret, frame = self.camera.get_frame()
        if not ret or frame is None:
            return None

        prediction = self.model.predict((ret, frame))
        if prediction == 1:
            self.class_label.config(text=self.classname_one)
            return self.classname_one
        elif prediction == 2:
            self.class_label.config(text=self.classname_two)
            return self.classname_two
        return None
