# 💻 Laptop Price Prediction in Python

A machine learning project that predicts the **price of a laptop** using Python and common data science tools.  
This project follows the YouTube tutorial *Laptop Price Prediction with Python (NeuralNine)*.
---

## 📌 Project Overview

The goal of this project is to build a regression model that can estimate the price of a laptop based on its specifications, such as brand, processor, RAM, storage, GPU, etc.

This kind of model can be useful for:
- Helping users estimate the fair price of a laptop  
- Building price recommendation systems  
- Understanding the impact of hardware specs on pricing

---

## 🛠 How It Works

1. **Load the dataset**  
   - Laptop specifications and prices are loaded into a pandas DataFrame.

2. **Data Cleaning & Feature Engineering**  
   - Missing values are handled.
   - Categorical features (e.g., brand, CPU type) are encoded into numerical values.

3. **Model Training**  
   - A regression model (e.g., Random Forest Regressor) is trained on the training data.
   - Models are evaluated using metrics like R² and RMSE.

4. **Predictions**  
   - The trained model predicts prices for new laptop specifications.

5. **Exporting the Model**  
   - The final model may be saved using joblib or pickle for reuse in applications.

---

## 🧠 Libraries & Tools Used

- Python 3  
- pandas — data manipulation  
- numpy — numerical operations  
- scikit‑learn — machine learning models and preprocessing  
- matplotlib / seaborn — optional for visualization  
- joblib / pickle — model saving

---

## 📚 Things Learned

- How to handle real‑world datasets in Python  
- Feature preprocessing and encoding  
- Training and evaluating regression models  
- The importance of feature selection
- Saving and loading machine learning models

---

## 🧾 Credits

- 📹 **Video Credits:** [Laptop Price Prediction with Python by NeuralNine](https://www.youtube.com/watch?v=A1eU51jPpXQ)
- 🤖 **README file:** Done with the help of ChatGPT  

---
