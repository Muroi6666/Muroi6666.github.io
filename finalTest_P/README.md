# finalTest_P 실습시험 참고

이 폴더는 실습시험 때 참고하기 위한 머신러닝 분류 코드 예시입니다. CSV 파일은 GitHub에 올리지 않고, 코드와 실행 방법만 정리합니다.

## 핵심 흐름

1. `pandas`로 CSV 파일을 불러옵니다.
2. 사용할 feature 컬럼과 정답 target 컬럼을 정합니다.
3. `RandomForestClassifier` 모델을 학습합니다.
4. `accuracy_score`, `confusion_matrix`, `classification_report`로 결과를 확인합니다.
5. 테스트 데이터를 예측해 `prediction` 컬럼을 만듭니다.
6. `to_csv(index=False)`로 제출 파일을 저장합니다.
7. `joblib.dump()`로 모델을 저장합니다.

## 사용한 라이브러리

| 라이브러리 | 사용 목적 |
| --- | --- |
| `pandas` | CSV 읽기, 컬럼 선택, 결과 저장 |
| `scikit-learn` | RandomForest 모델 학습과 평가 |
| `joblib` | 모델 저장 및 불러오기 |
| `pathlib` | 파일 경로 관리 |

## 사용한 모델

- 기업이 아니라 기법/라이브러리 기준으로는 `scikit-learn`의 `RandomForestClassifier`를 사용했습니다.
- 저장 모델 파일은 `best_model.pkl`입니다.

## 시험장에서 주로 수정할 부분

```python
FEATURES = [
    "study_hours",
    "sleep_hours",
    "attendance_rate",
    "assignments_completed",
    "screen_time_hours",
]

TARGET = "pass"
```

시험 데이터의 컬럼명이 다르면 위의 `FEATURES`와 `TARGET`을 먼저 바꾸면 됩니다.

## 실행 코드

```bash
python train_and_predict.py
```

같은 폴더에 `train_practice.csv`와 `test_practice.csv`가 있으면 모델 학습, 테스트 예측, 결과 CSV 저장, 모델 저장까지 한 번에 실행됩니다.
