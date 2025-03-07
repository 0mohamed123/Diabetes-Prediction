import sys
import joblib
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class DiabetesPredictor(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Diabetes Prediction")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        self.labels = ["Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness", "Insulin", "BMI", "Diabetes Pedigree Function", "Age"]
        self.inputs = []

        for label in self.labels:
            layout.addWidget(QLabel(label))
            line_edit = QLineEdit()
            self.inputs.append(line_edit)
            layout.addWidget(line_edit)

        self.predict_btn = QPushButton("Predict")
        self.predict_btn.clicked.connect(self.make_prediction)
        layout.addWidget(self.predict_btn)

        self.setLayout(layout)

    def make_prediction(self):
        try:
            data = [float(input.text()) for input in self.inputs]
            model = joblib.load("diabetes_model.pkl")
            prediction = model.predict([data])

            result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"
            QMessageBox.information(self, "Prediction Result", f"Result: {result}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid input: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiabetesPredictor()
    window.show()
    sys.exit(app.exec())