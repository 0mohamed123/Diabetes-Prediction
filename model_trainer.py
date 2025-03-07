import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from data_loader import load_data

def train_model():
    X_train, X_test, y_train, y_test = load_data()

    # تدريب النموذج
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # تقييم النموذج
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    # حفظ النموذج
    joblib.dump(model, "diabetes_model.pkl")

    return model

if __name__ == "__main__":
    train_model()