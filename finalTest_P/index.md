---
layout: default
title: finalTest_P
---

# finalTest_P 학생 합격 예측

학생의 학습 습관 데이터를 이용해 합격 여부(`pass`)를 예측하는 머신러닝 분류 실습입니다.

CSV 데이터 파일은 GitHub Pages에 공개하지 않고, 코드와 실행 결과 요약만 정리했습니다.

## 파일 구성

| 파일 | 설명 |
| --- | --- |
| `A.ipynb` | 데이터 확인, 모델 평가, 예측 결과 요약 노트북 |
| `train_and_predict.py` | 모델 학습과 테스트 예측 실행 코드 |
| `best_model.pkl` | 학습된 RandomForest 모델 |
| `README.md` | 저장소용 프로젝트 요약 문서 |

## 사용 데이터 요약

| 데이터 | 크기 | 설명 |
| --- | ---: | --- |
| `train_practice.csv` | 300행, 11열 | 학습 데이터 |
| `test_practice.csv` | 20행, 10열 | 예측 대상 데이터 |
| `submit_result.csv` | 20행, 11열 | 예측 결과 데이터 |

## 모델 정보

- 모델: `RandomForestClassifier`
- 설정: `random_state=42`, `n_estimators=100`, `max_features="sqrt"`
- 타깃 컬럼: `pass`

학습에 사용한 5개 입력 컬럼은 아래와 같습니다.

| 컬럼 | 설명 |
| --- | --- |
| `study_hours` | 공부 시간 |
| `sleep_hours` | 수면 시간 |
| `attendance_rate` | 출석률 |
| `assignments_completed` | 과제 완료율 |
| `screen_time_hours` | 화면 사용 시간 |

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

## 테스트 예측 결과

테스트 데이터 20건에 대한 예측 분포입니다.

| prediction | 개수 |
| ---: | ---: |
| 0 | 4 |
| 1 | 16 |

## 실행 방법

```bash
python train_and_predict.py
```

같은 폴더에 `train_practice.csv`와 `test_practice.csv`가 있으면 모델을 학습하고, 예측 결과를 `submit_result.csv`로 저장합니다.

[GitHub 저장소에서 파일 보기](https://github.com/Muroi6666/Muroi6666.github.io/tree/main/finalTest_P)
