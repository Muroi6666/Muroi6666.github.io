---
layout: default
title: finalTest_P 실습시험 참고
---

# finalTest_P 실습시험 참고

이 페이지는 실습시험 때 블로그를 보면서 바로 따라 하기 위한 코드 정리입니다.

목표는 CSV 파일을 불러오고, 필요한 feature를 고른 뒤, 머신러닝 모델을 학습하고, 테스트 데이터 예측 결과를 CSV로 저장하는 것입니다.

## 사용한 라이브러리와 기법

| 구분 | 사용한 것 | 용도 |
| --- | --- | --- |
| 데이터 처리 | `pandas` | CSV 불러오기, 컬럼 선택, 결과 저장 |
| 경로 처리 | `pathlib.Path` | 현재 파일 기준으로 CSV/모델 경로 만들기 |
| 모델 | `RandomForestClassifier` | 합격 여부 분류 모델 학습 |
| 평가 | `accuracy_score`, `confusion_matrix`, `classification_report` | 학습 결과 확인 |
| 모델 저장 | `joblib` | 학습된 모델을 `.pkl` 파일로 저장 |

기업을 사용한 것이 아니라, 파이썬 머신러닝 라이브러리인 `scikit-learn`의 `RandomForestClassifier` 기법을 사용했습니다.

## 전체 실습 순서

1. 필요한 라이브러리를 import합니다.
2. 학습 CSV와 테스트 CSV 경로를 지정합니다.
3. 학습에 사용할 feature 5개와 정답 컬럼을 정합니다.
4. `pd.read_csv()`로 데이터를 불러옵니다.
5. `X`, `y`를 나누어 모델을 학습합니다.
6. 학습 데이터 기준으로 정확도와 리포트를 확인합니다.
7. 테스트 데이터에 `prediction` 컬럼을 추가합니다.
8. `submit_result.csv`로 저장합니다.
9. 학습된 모델을 `best_model.pkl`로 저장합니다.

## 1. 라이브러리 import

```python
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
```

## 2. 파일 경로 지정

```python
BASE_DIR = Path(__file__).resolve().parent
TRAIN_PATH = BASE_DIR / "train_practice.csv"
TEST_PATH = BASE_DIR / "test_practice.csv"
MODEL_PATH = BASE_DIR / "best_model.pkl"
SUBMIT_PATH = BASE_DIR / "submit_result.csv"
```

노트북에서는 `__file__`을 사용할 수 없으므로 아래처럼 써도 됩니다.

```python
TRAIN_PATH = "train_practice.csv"
TEST_PATH = "test_practice.csv"
MODEL_PATH = "best_model.pkl"
SUBMIT_PATH = "submit_result.csv"
```

## 3. feature와 target 정하기

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

시험에서 컬럼명이 다르면 `FEATURES`와 `TARGET`만 시험 데이터에 맞게 바꾸면 됩니다.

## 4. CSV 불러오기

```python
train_df = pd.read_csv(TRAIN_PATH)
test_df = pd.read_csv(TEST_PATH)

print(train_df.shape)
print(test_df.shape)
print(train_df.columns)
```

컬럼명 확인은 꼭 해야 합니다. 오타가 있으면 모델 학습 전에 에러가 납니다.

## 5. X, y 나누기

```python
x_train = train_df[FEATURES]
y_train = train_df[TARGET]
```

`x_train`에는 문제 데이터, `y_train`에는 정답 데이터가 들어갑니다.

## 6. 모델 만들고 학습하기

```python
model = RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)
```

`random_state=42`를 넣으면 실행할 때마다 결과가 크게 흔들리지 않습니다.

## 7. 학습 결과 확인하기

```python
train_pred = model.predict(x_train)

print(f"Accuracy: {accuracy_score(y_train, train_pred):.4f}")
print("Confusion matrix:")
print(confusion_matrix(y_train, train_pred))
print("Classification report:")
print(classification_report(y_train, train_pred, digits=4))
```

시험에서 평가 지표를 물어보면 `classification_report`의 `macro avg`, `weighted avg`, `f1-score`를 확인하면 됩니다.

## 8. 테스트 데이터 예측하기

```python
result_df = test_df.copy()
result_df["prediction"] = model.predict(test_df[FEATURES])
```

테스트 데이터에는 정답 컬럼이 없으므로 `FEATURES` 컬럼만 넣어 예측합니다.

## 9. 제출 CSV 저장하기

```python
result_df.to_csv(SUBMIT_PATH, index=False)
```

`index=False`를 넣어야 불필요한 인덱스 컬럼이 CSV에 추가되지 않습니다.

## 10. 모델 저장하기

```python
joblib.dump(model, MODEL_PATH)
```

저장한 모델은 나중에 아래처럼 다시 불러올 수 있습니다.

```python
model = joblib.load("best_model.pkl")
```

## 한 번에 실행하는 전체 코드

```python
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

train_df = pd.read_csv(TRAIN_PATH)
test_df = pd.read_csv(TEST_PATH)

x_train = train_df[FEATURES]
y_train = train_df[TARGET]

model = RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)

train_pred = model.predict(x_train)
print(f"Accuracy: {accuracy_score(y_train, train_pred):.4f}")
print(confusion_matrix(y_train, train_pred))
print(classification_report(y_train, train_pred, digits=4))

result_df = test_df.copy()
result_df["prediction"] = model.predict(test_df[FEATURES])
result_df.to_csv(SUBMIT_PATH, index=False)

joblib.dump(model, MODEL_PATH)
```

## 시험장에서 바꿀 가능성이 높은 부분

| 상황 | 바꿀 코드 |
| --- | --- |
| 학습 파일 이름이 다름 | `TRAIN_PATH = "새파일명.csv"` |
| 테스트 파일 이름이 다름 | `TEST_PATH = "새파일명.csv"` |
| 정답 컬럼 이름이 다름 | `TARGET = "정답컬럼명"` |
| 사용할 feature가 다름 | `FEATURES = [...]` 안의 컬럼명 수정 |
| 결과 파일 이름을 바꿔야 함 | `SUBMIT_PATH = "제출파일명.csv"` |

## 자주 나는 에러 체크

| 에러 상황 | 확인할 것 |
| --- | --- |
| 컬럼이 없다고 나옴 | `print(train_df.columns)`로 실제 컬럼명 확인 |
| 테스트 예측에서 에러남 | 학습 때 쓴 `FEATURES`와 테스트 컬럼명이 같은지 확인 |
| CSV에 이상한 첫 컬럼이 생김 | `to_csv(..., index=False)`를 썼는지 확인 |
| 모델 저장이 안 됨 | `import joblib` 했는지 확인 |
| 점수가 너무 이상함 | `TARGET`에 정답 컬럼을 제대로 넣었는지 확인 |

## 현재 실습 결과

| 항목 | 값 |
| --- | ---: |
| 학습 데이터 | 300행 |
| 테스트 데이터 | 20행 |
| Accuracy | 1.0000 |
| 예측 0 개수 | 4 |
| 예측 1 개수 | 16 |

[GitHub 저장소에서 코드 보기](https://github.com/Muroi6666/Muroi6666.github.io/tree/main/finalTest_P)
