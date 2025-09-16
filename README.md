# Diabetes Prediction

## 📌 Overview
This project aims to predict whether a person has diabetes or not using machine learning algorithms. The dataset used is the **PIMA Indians Diabetes Dataset**, which contains medical information of patients.

## 📊 Dataset
- **Source:** Kaggle / UCI Repository  
- **Features:**
  - Pregnancies  
  - Glucose  
  - Blood Pressure  
  - Skin Thickness  
  - Insulin  
  - BMI  
  - Diabetes Pedigree Function  
  - Age  
- **Target:** Outcome (0 = Non-Diabetic, 1 = Diabetic)

## ⚙️ Methodology
1. Data preprocessing (handling missing values, normalization).  
2. Train-test split for evaluation.  
3. Applied ML models such as:
   - Logistic Regression  
   - Random Forest  
   - Support Vector Machine (SVM)  
4. Evaluated using Accuracy, Precision, Recall, and F1-Score.

## 📈 Results
- The best-performing model achieved **XX% Accuracy**.  
- Confusion matrix and classification report included in the notebook.

## 🚀 Future Work
- Improve accuracy with deep learning models.  
- Deploy the model as a web app for real-time prediction.  

## 🛠️ Requirements

```bash
pip install numpy pandas scikit-learn matplotlib seaborn pyqt
```

## 📂 Project Structure

Diabetes-Prediction/

│── data_loader.py

│── diabetes.csv

│── gui.py

│── model_trainer.py

│── predictor.py

│── report.pdf

│── README.md

## 👨‍💻 Author

- Mohamed Kasm

## 📜 License

This project is licensed under the MIT License.
