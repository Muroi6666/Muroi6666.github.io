from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


BASE_DIR = Path(__file__).resolve().parent
TRAIN_DATA = BASE_DIR / "sample_train.csv"
MODEL_PATH = BASE_DIR / "best_model.joblib"
TARGET_COLUMN = "target"


def make_five_features(df: pd.DataFrame) -> pd.DataFrame:
    """원본 10개 feature에서 최종 학습용 5개 feature만 생성합니다."""
    selected = pd.DataFrame(index=df.index)
    selected["feature_01"] = df["feature_01"]
    selected["feature_03"] = df["feature_03"]
    selected["feature_07"] = df["feature_07"]
    selected["combo_01_02_mean"] = (df["feature_01"] + df["feature_02"]) / 2
    selected["combo_04_05_ratio"] = df["feature_04"] / (df["feature_05"] + 1e-6)
    return selected


def build_candidates() -> dict[str, Pipeline]:
    return {
        "logistic_regression": Pipeline(
            [
                ("scaler", StandardScaler()),
                ("model", LogisticRegression(max_iter=1000, random_state=42)),
            ]
        ),
        "random_forest": Pipeline(
            [
                (
                    "model",
                    RandomForestClassifier(
                        n_estimators=200,
                        max_depth=4,
                        random_state=42,
                    ),
                )
            ]
        ),
        "gradient_boosting": Pipeline(
            [
                (
                    "model",
                    GradientBoostingClassifier(
                        n_estimators=100,
                        learning_rate=0.05,
                        max_depth=2,
                        random_state=42,
                    ),
                )
            ]
        ),
    }


def main() -> None:
    df = pd.read_csv(TRAIN_DATA)
    x = make_five_features(df)
    y = df[TARGET_COLUMN]

    x_train, x_valid, y_train, y_valid = train_test_split(
        x,
        y,
        test_size=0.3,
        random_state=42,
        stratify=y,
    )

    best_name = ""
    best_score = -1.0
    best_model = None

    print("사용한 최종 feature 5개:", list(x.columns))
    print()

    for name, model in build_candidates().items():
        model.fit(x_train, y_train)
        pred = model.predict(x_valid)
        macro_f1 = f1_score(y_valid, pred, average="macro")

        print(f"[{name}] macro avg f1-score: {macro_f1:.4f}")
        print(classification_report(y_valid, pred, digits=4))

        if macro_f1 > best_score:
            best_name = name
            best_score = macro_f1
            best_model = model

    if best_model is None:
        raise RuntimeError("학습된 모델이 없습니다.")

    artifact = {
        "model_name": best_name,
        "macro_f1": best_score,
        "feature_names": list(x.columns),
        "model": best_model,
    }
    joblib.dump(artifact, MODEL_PATH)

    print(f"최적 모델: {best_name}")
    print(f"최적 macro avg f1-score: {best_score:.4f}")
    print(f"저장 위치: {MODEL_PATH}")


if __name__ == "__main__":
    main()
