import joblib
import numpy as np

def predict_diabetes(data):
    model = joblib.load("diabetes_model.pkl")
    prediction = model.predict([data])
    return "Diabetic" if prediction[0] == 1 else "Non-Diabetic"

if __name__ == "__main__":
    sample_data = [6, 148, 72, 35, 0, 33.6, 0.627, 50]  # مثال لبيانات مريض
    result = predict_diabetes(sample_data)
    print(f"Prediction: {result}")