---
layout: default
title: 기말고사실습
---

# 기말고사실습

기말고사 조건에 맞춰 머신러닝 분류 모델을 학습하고, 저장된 최적 모델로 테스트 데이터를 예측하는 예시입니다.

이 자료의 목적은 `macro avg f1-score`를 무조건 1.0으로 만드는 것이 아니라, 시험장에서 제공된 데이터로 조건을 빠뜨리지 않고 구현하는 방법을 쉽게 따라 하는 것입니다.

## 과제 조건 대응

| 조건 | 구현 파일 | 설명 |
| --- | --- | --- |
| 10개 feature 중 5개만 활용 | `train_model.py` | 원본 feature 3개와 조합 feature 2개를 사용합니다. |
| 선정/조합된 5개 feature로 모델 학습 | `train_model.py` | Logistic Regression, Random Forest, Gradient Boosting을 비교합니다. |
| 최적 모델 1개 저장 | `train_model.py` | macro avg f1-score가 가장 높은 모델을 `best_model.joblib`로 저장합니다. |
| 저장 모델을 불러와 테스트 실행 환경 구축 | `realtime_predict.py` | 저장 모델과 feature 변환기를 불러옵니다. |
| test 데이터 실시간 구동 | `realtime_predict.py` | 새 CSV를 넣으면 즉시 예측 결과 CSV를 생성합니다. |

## 파일 구성

| 파일 | 역할 |
| --- | --- |
| `sample_train.csv` | 학습용 예시 데이터입니다. feature 10개와 target 1개가 있습니다. |
| `sample_test.csv` | 제출 전 테스트용 예시 데이터입니다. target 없이 feature 10개만 있습니다. |
| `train_model.py` | 5개 feature 생성, 모델 학습, macro avg f1-score 평가, 최적 모델 저장을 수행합니다. |
| `realtime_predict.py` | 저장된 모델을 불러와 테스트 CSV를 예측합니다. |
| `requirements.txt` | 실행에 필요한 파이썬 패키지 목록입니다. |

## 전체 흐름

시험에서는 보통 학습용 데이터와 테스트용 데이터를 따로 받습니다. 아래 순서대로 진행하면 됩니다.

1. 학습용 CSV 파일을 확인합니다.
2. 전체 feature 10개 중에서 사용할 feature 5개를 정합니다.
3. 원본 feature를 그대로 써도 되고, 여러 feature를 조합해서 새 feature를 만들어도 됩니다.
4. 선택한 5개 feature만 가지고 여러 모델을 학습합니다.
5. 검증 데이터에서 `macro avg f1-score`가 가장 좋은 모델 하나를 고릅니다.
6. 고른 모델을 `best_model.joblib`로 저장합니다.
7. 테스트 CSV가 주어지면 저장된 모델을 불러와 예측합니다.

## 실행 방법

```bash
pip install -r requirements.txt
python train_model.py
python realtime_predict.py --input sample_test.csv --output predictions.csv
```

## 사용한 5개 feature

원본 데이터에는 `feature_01`부터 `feature_10`까지 10개의 feature가 있습니다. 실제 학습에는 아래 5개만 사용합니다.

| 학습 feature | 종류 | 설명 |
| --- | --- | --- |
| `feature_01` | 원본 | 첫 번째 원본 feature |
| `feature_03` | 원본 | 세 번째 원본 feature |
| `feature_07` | 원본 | 일곱 번째 원본 feature |
| `combo_01_02_mean` | 조합 | `feature_01`과 `feature_02`의 평균 |
| `combo_04_05_ratio` | 조합 | `feature_04 / (feature_05 + 1e-6)` |

중요한 점은 최종적으로 모델에 들어가는 컬럼 수가 정확히 5개여야 한다는 것입니다. 그래서 `train_model.py`의 `make_five_features()` 함수가 5개 컬럼만 반환하도록 만들었습니다.

```python
def make_five_features(df):
    selected = pd.DataFrame(index=df.index)
    selected["feature_01"] = df["feature_01"]
    selected["feature_03"] = df["feature_03"]
    selected["feature_07"] = df["feature_07"]
    selected["combo_01_02_mean"] = (df["feature_01"] + df["feature_02"]) / 2
    selected["combo_04_05_ratio"] = df["feature_04"] / (df["feature_05"] + 1e-6)
    return selected
```

## 시험 데이터로 바꾸는 방법

시험에서 받은 학습 데이터 파일명이 `train.csv`라면 `train_model.py`에서 아래 부분만 바꾸면 됩니다.

```python
TRAIN_DATA = BASE_DIR / "sample_train.csv"
```

예를 들어 같은 폴더에 `train.csv`를 넣었다면 이렇게 바꿉니다.

```python
TRAIN_DATA = BASE_DIR / "train.csv"
```

정답 컬럼 이름이 `target`이 아니라 `label`, `class`, `y` 같은 이름이면 아래 부분도 바꿉니다.

```python
TARGET_COLUMN = "target"
```

예를 들어 정답 컬럼 이름이 `label`이면 이렇게 바꿉니다.

```python
TARGET_COLUMN = "label"
```

테스트 데이터 파일명이 `test.csv`라면 예측할 때 이렇게 실행합니다.

```bash
python realtime_predict.py --input test.csv --output predictions.csv
```

## feature를 바꾸는 방법

시험 데이터의 컬럼명이 예시와 다를 수 있습니다. 그럴 때는 `make_five_features()` 함수 안의 컬럼 이름을 시험 데이터에 맞게 바꾸면 됩니다.

예를 들어 시험 데이터에 `age`, `income`, `score`, `visit_count`, `buy_count` 같은 컬럼이 있다면 아래처럼 바꿀 수 있습니다.

```python
def make_five_features(df):
    selected = pd.DataFrame(index=df.index)
    selected["age"] = df["age"]
    selected["income"] = df["income"]
    selected["score"] = df["score"]
    selected["visit_per_buy"] = df["visit_count"] / (df["buy_count"] + 1e-6)
    selected["income_score"] = df["income"] * df["score"]
    return selected
```

이 경우에도 최종 feature는 `age`, `income`, `score`, `visit_per_buy`, `income_score` 총 5개입니다.

## 채점 핵심

평가 지표는 `macro avg f1-score`입니다. `train_model.py`는 `classification_report`와 함께 macro f1 값을 출력하고, 가장 높은 모델 하나만 저장합니다.

`macro avg f1-score`는 각 클래스를 똑같이 중요하게 보고 평균을 내는 점수입니다. 데이터에 특정 클래스가 많고 다른 클래스가 적어도, 소수 클래스 성능까지 같이 반영됩니다.

## 감점 방지 체크리스트

제출 또는 시연 전에 아래를 확인합니다.

- 최종 학습 feature가 정확히 5개인지 확인합니다.
- 학습할 때 사용한 feature 생성 방식과 테스트할 때 사용한 feature 생성 방식이 같은지 확인합니다.
- `best_model.joblib` 파일이 생성됐는지 확인합니다.
- 테스트 예측은 `train_model.py`가 아니라 `realtime_predict.py`로 실행합니다.
- 결과 파일 `predictions.csv`에 `prediction` 컬럼이 생겼는지 확인합니다.
- `classification_report` 출력에서 `macro avg`의 `f1-score` 값을 확인합니다.

## 시험장에서 최소 수정할 부분

대부분의 경우 아래 세 가지만 바꾸면 됩니다.

1. `TRAIN_DATA`: 학습 데이터 파일명
2. `TARGET_COLUMN`: 정답 컬럼명
3. `make_five_features()`: 시험 데이터에 맞는 feature 5개

나머지 모델 학습, 점수 비교, 모델 저장, 테스트 예측 코드는 그대로 사용하면 됩니다.
