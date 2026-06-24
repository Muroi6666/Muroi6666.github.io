---
layout: default
title: finalTest_P 실습시험 참고
---

# finalTest_P 실습시험 참고

이 페이지는 실습시험 때 블로그를 보면서 바로 따라 하기 위한 코드 정리입니다.

목표는 CSV 파일을 불러오고, 필요한 feature를 고른 뒤, 머신러닝 모델을 학습하고, 테스트 데이터 예측 결과를 CSV로 저장하는 것입니다.

## 초보자용 큰 그림

이 실습은 한 문장으로 말하면 **학생 정보로 합격 여부를 예측하는 모델을 만드는 과정**입니다.

머신러닝에서는 보통 데이터를 두 부분으로 나눕니다.

| 이름 | 뜻 | 이 실습 예시 |
| --- | --- | --- |
| `X` | 문제, 입력 데이터 | 공부 시간, 수면 시간, 출석률 같은 컬럼 |
| `y` | 정답, 예측해야 하는 값 | `pass` 컬럼 |

즉, 모델에게 `X`를 보여주면서 `y`를 맞히도록 학습시키는 것입니다.

```python
X = df[features]
y = df["pass"]
```

위 코드는 `features`에 적어둔 컬럼들을 문제로 사용하고, `pass` 컬럼을 정답으로 사용한다는 뜻입니다.

## A.ipynb 코드 흐름

현재 노트북은 아래 순서로 보면 됩니다.

1. `train_practice.csv`를 불러옵니다.
2. 사용할 feature 5개를 고릅니다.
3. `X`와 `y`로 데이터를 나눕니다.
4. `train_test_split`으로 학습용/검증용 데이터를 나눕니다.
5. `RandomForestClassifier` 모델을 학습합니다.
6. `classification_report`로 점수를 확인합니다.
7. `joblib.dump()`로 모델을 저장합니다.
8. `test_practice.csv`를 불러와 예측합니다.
9. `prediction` 컬럼을 붙여 `submit_result.csv`로 저장합니다.

시험 때는 이 순서를 크게 벗어나지 않으면 됩니다.

## 사용한 라이브러리와 기법

| 구분 | 사용한 것 | 용도 |
| --- | --- | --- |
| 데이터 처리 | `pandas` | CSV 불러오기, 컬럼 선택, 결과 저장 |
| 경로 처리 | `pathlib.Path` | 현재 파일 기준으로 CSV/모델 경로 만들기 |
| 데이터 분리 | `train_test_split` | 학습용 데이터와 검증용 데이터 나누기 |
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
6. `train_test_split`으로 연습용 문제와 확인용 문제를 나눕니다.
7. 학습 결과를 `classification_report`로 확인합니다.
8. 학습된 모델을 `best_model.pkl`로 저장합니다.
9. 테스트 데이터에 `prediction` 컬럼을 추가합니다.
10. `submit_result.csv`로 저장합니다.

## 1. 라이브러리 import

```python
from pathlib import Path

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
```

처음에는 import가 낯설 수 있는데, 쉽게 생각하면 **필요한 도구를 꺼내 오는 코드**입니다.

- `pandas`: CSV 파일을 표처럼 다루는 도구
- `train_test_split`: 데이터를 학습용과 테스트용으로 나누는 도구
- `RandomForestClassifier`: 분류 문제를 푸는 머신러닝 모델
- `classification_report`: 모델 점수를 보기 좋게 출력하는 도구
- `joblib`: 학습한 모델을 파일로 저장하는 도구

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

여기서 중요한 점은 `FEATURES`에는 정답 컬럼을 넣으면 안 된다는 것입니다. 정답 컬럼인 `pass`는 `TARGET`에 따로 적습니다.

## 4. CSV 불러오기

```python
train_df = pd.read_csv(TRAIN_PATH)
test_df = pd.read_csv(TEST_PATH)

print(train_df.shape)
print(test_df.shape)
print(train_df.columns)
```

컬럼명 확인은 꼭 해야 합니다. 오타가 있으면 모델 학습 전에 에러가 납니다.

처음 데이터를 불러온 뒤에는 아래 두 줄을 자주 사용합니다.

```python
print(train_df.head())
print(train_df.columns)
```

- `head()`는 위에서 5줄만 보여줍니다.
- `columns`는 컬럼 이름을 보여줍니다.

시험장에서 컬럼 이름이 기억나지 않으면 먼저 이 코드를 실행해서 확인하면 됩니다.

## 5. X, y 나누기

```python
x_train = train_df[FEATURES]
y_train = train_df[TARGET]
```

`x_train`에는 문제 데이터, `y_train`에는 정답 데이터가 들어갑니다.

노트북에서는 변수 이름을 짧게 `X`, `y`로 써도 됩니다.

```python
X = df[features]
y = df["pass"]
```

둘은 같은 의미입니다. `X`는 대문자, `y`는 소문자로 많이 씁니다.

## 6. 학습용/검증용 데이터 나누기

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

이 코드는 전체 학습 데이터를 다시 두 덩어리로 나누는 코드입니다.

| 변수 | 의미 |
| --- | --- |
| `X_train` | 모델이 공부할 문제 |
| `y_train` | 모델이 공부할 정답 |
| `X_test` | 모델이 맞혀볼 검증 문제 |
| `y_test` | 검증 문제의 실제 정답 |

`test_size=0.2`는 전체 데이터 중 20%를 검증용으로 쓰겠다는 뜻입니다.

## 7. 모델 만들고 학습하기

```python
model = RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)
```

`random_state=42`를 넣으면 실행할 때마다 결과가 크게 흔들리지 않습니다.

노트북처럼 `X_train`, `y_train`을 썼다면 아래처럼 작성합니다.

```python
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
```

`fit()`은 모델에게 공부시키는 명령입니다.

## 8. 학습 결과 확인하기

```python
train_pred = model.predict(x_train)

print(f"Accuracy: {accuracy_score(y_train, train_pred):.4f}")
print("Confusion matrix:")
print(confusion_matrix(y_train, train_pred))
print("Classification report:")
print(classification_report(y_train, train_pred, digits=4))
```

시험에서 평가 지표를 물어보면 `classification_report`의 `macro avg`, `weighted avg`, `f1-score`를 확인하면 됩니다.

노트북처럼 검증 데이터 기준으로 확인한다면 아래처럼 작성합니다.

```python
pred = model.predict(X_test)
print(classification_report(y_test, pred))
```

`predict()`는 모델에게 문제를 풀어보라고 시키는 명령입니다.

## 9. 테스트 데이터 예측하기

```python
result_df = test_df.copy()
result_df["prediction"] = model.predict(test_df[FEATURES])
```

테스트 데이터에는 정답 컬럼이 없으므로 `FEATURES` 컬럼만 넣어 예측합니다.

노트북처럼 저장한 모델을 다시 불러와서 예측할 수도 있습니다.

```python
loaded_model = joblib.load("best_model.pkl")
test_df = pd.read_csv("test_practice.csv")
test_X = test_df[features]
result = loaded_model.predict(test_X)
```

## 10. 제출 CSV 저장하기

```python
result_df.to_csv(SUBMIT_PATH, index=False)
```

`index=False`를 넣어야 불필요한 인덱스 컬럼이 CSV에 추가되지 않습니다.

노트북처럼 `test_df`에 바로 붙여도 됩니다.

```python
test_df["prediction"] = result
test_df.to_csv("submit_result.csv", index=False)
```

## 11. 모델 저장하기

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
from sklearn.model_selection import train_test_split
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

X_train, X_test, y_train_split, y_test = train_test_split(
    x_train,
    y_train,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train_split)

pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, pred):.4f}")
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred, digits=4))

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
| 검증 Accuracy | 0.9000 |
| 검증 Macro F1-score | 0.78 |
| 예측 0 개수 | 3 |
| 예측 1 개수 | 17 |

[GitHub 저장소에서 코드 보기](https://github.com/Muroi6666/Muroi6666.github.io/tree/main/finalTest_P)
