import argparse
from pathlib import Path

import joblib
import pandas as pd

from train_model import BASE_DIR, MODEL_PATH, make_five_features


def predict(input_path: Path, output_path: Path) -> None:
    artifact = joblib.load(MODEL_PATH)
    model = artifact["model"]
    expected_features = artifact["feature_names"]

    test_df = pd.read_csv(input_path)
    x_test = make_five_features(test_df)
    x_test = x_test[expected_features]

    result = test_df.copy()
    result["prediction"] = model.predict(x_test)

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(x_test)
        for class_index, class_label in enumerate(model.classes_):
            result[f"prob_class_{class_label}"] = probabilities[:, class_index]

    result.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"모델 이름: {artifact['model_name']}")
    print(f"검증 macro avg f1-score: {artifact['macro_f1']:.4f}")
    print(f"예측 결과 저장: {output_path}")
    print(result)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="저장된 최적 모델로 테스트 데이터를 예측합니다.")
    parser.add_argument(
        "--input",
        default=str(BASE_DIR / "sample_test.csv"),
        help="테스트 CSV 경로",
    )
    parser.add_argument(
        "--output",
        default=str(BASE_DIR / "predictions.csv"),
        help="예측 결과 CSV 저장 경로",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"{MODEL_PATH} 파일이 없습니다. 먼저 python train_model.py를 실행하세요."
        )

    predict(input_path, output_path)


if __name__ == "__main__":
    main()
