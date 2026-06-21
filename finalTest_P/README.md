# finalTest_P 학생 합격 예측 요약

## 프로젝트 개요

학생의 학습 습관 데이터를 이용해 합격 여부(`pass`)를 예측하는 분류 실습입니다. 학습 데이터와 테스트 데이터 CSV는 개인정보/용량 관리를 위해 GitHub에는 올리지 않고, 코드와 모델 파일, 결과 요약만 저장합니다.

## 사용 데이터

- 학습 데이터: `train_practice.csv` 300행, 11열
- 테스트 데이터: `test_practice.csv` 20행, 10열
- 제출 결과: `submit_result.csv` 20행, 11열
- 타깃 컬럼: `pass`

CSV 파일은 `.gitignore`로 제외되어 있으며 로컬 실행 시 같은 폴더에 두면 됩니다.

## 모델

- 모델: `RandomForestClassifier`
- 주요 설정: `random_state=42`, `n_estimators=100`, `max_features="sqrt"`
- 저장 파일: `best_model.pkl`
- 학습에 사용한 입력 컬럼:
  - `study_hours`
  - `sleep_hours`
  - `attendance_rate`
  - `assignments_completed`
  - `screen_time_hours`

## 학습 데이터 기준 성능

| 지표 | 값 |
| --- | ---: |
| Accuracy | 1.0000 |
| Macro F1-score | 1.0000 |
| Weighted F1-score | 1.0000 |

혼동 행렬:

| 실제 \ 예측 | 0 | 1 |
| --- | ---: | ---: |
| 0 | 42 | 0 |
| 1 | 0 | 258 |

## 변수 중요도

| 순위 | 변수 | 중요도 |
| ---: | --- | ---: |
| 1 | `study_hours` | 0.4383 |
| 2 | `attendance_rate` | 0.1648 |
| 3 | `assignments_completed` | 0.1621 |
| 4 | `screen_time_hours` | 0.1476 |
| 5 | `sleep_hours` | 0.0873 |

## 테스트 예측 결과 요약

테스트 데이터 20건에 대한 예측 분포는 다음과 같습니다.

| prediction | 개수 |
| ---: | ---: |
| 0 | 4 |
| 1 | 16 |

## 실행 방법

```bash
python train_and_predict.py
```

실행하면 `train_practice.csv`를 이용해 모델을 학습하고, `test_practice.csv`에 대한 예측 결과를 `submit_result.csv`로 저장합니다.
