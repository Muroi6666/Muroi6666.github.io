from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


BASE_DIR = Path(__file__).resolve().parent
TRAIN_PATH = BASE_DIR / "train_practice.csv"
TEST_PATH = BASE_DIR / "test_practice.csv"
MODEL_PATH = BASE_DIR / "best_model.pkl"
SUBMIT_PATH = BASE_DIR / "submit_result.csv"

FEATURES = [
    "study_hours",
    "sleep_hours",
    "attendance_rate",
    "assignments_completed",
    "screen_time_hours",
]
TARGET = "pass"


def main() -> None:
    train_df = pd.read_csv(TRAIN_PATH)
    test_df = pd.read_csv(TEST_PATH)

    x_train = train_df[FEATURES]
    y_train = train_df[TARGET]

    model = RandomForestClassifier(random_state=42)
    model.fit(x_train, y_train)

    train_pred = model.predict(x_train)
    print(f"Accuracy: {accuracy_score(y_train, train_pred):.4f}")
    print("Confusion matrix:")
    print(confusion_matrix(y_train, train_pred))
    print("Classification report:")
    print(classification_report(y_train, train_pred, digits=4))

    result_df = test_df.copy()
    result_df["prediction"] = model.predict(test_df[FEATURES])
    result_df.to_csv(SUBMIT_PATH, index=False)

    joblib.dump(model, MODEL_PATH)
    print(f"Saved model: {MODEL_PATH.name}")
    print(f"Saved predictions: {SUBMIT_PATH.name}")
    print("Prediction counts:")
    print(result_df["prediction"].value_counts().sort_index())


if __name__ == "__main__":
    main()
