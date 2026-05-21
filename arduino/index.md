---
layout: default
title: Arduino Study
---

# Arduino Study

아두이노 실습 내용을 날짜별로 정리하는 공간입니다.

## 실습 목록

- [2026-05-21 빨강, 노랑, 파랑 LED 1초 간격 점등](#2026-05-21-빨강-노랑-파랑-led-1초-간격-점등)

## 2026-05-21 빨강, 노랑, 파랑 LED 1초 간격 점등

### 실습 목표

빨강, 노랑, 파랑 LED를 각각 1초 간격으로 순서대로 켜고 끄는 회로와 코드를 작성한다.

### 사용 부품

- Arduino Uno
- 빨강 LED 1개
- 노랑 LED 1개
- 파랑 LED 1개
- 220옴 저항 3개
- 브레드보드
- 점퍼선

### 회로 연결

| LED 색상 | Arduino 핀 |
| --- | --- |
| 빨강 LED | 8번 핀 |
| 노랑 LED | 9번 핀 |
| 파랑 LED | 10번 핀 |

각 LED의 긴 다리(+)는 저항을 거쳐 Arduino 디지털 핀에 연결하고, 짧은 다리(-)는 GND에 연결한다.

### 예제 코드

```cpp
const int redLed = 8;
const int yellowLed = 9;
const int blueLed = 10;

void setup() {
  pinMode(redLed, OUTPUT);
  pinMode(yellowLed, OUTPUT);
  pinMode(blueLed, OUTPUT);
}

void loop() {
  digitalWrite(redLed, HIGH);
  delay(1000);
  digitalWrite(redLed, LOW);

  digitalWrite(yellowLed, HIGH);
  delay(1000);
  digitalWrite(yellowLed, LOW);

  digitalWrite(blueLed, HIGH);
  delay(1000);
  digitalWrite(blueLed, LOW);
}
```

### 실행 결과

빨강 LED가 1초 동안 켜진 뒤 꺼지고, 이어서 노랑 LED와 파랑 LED도 같은 방식으로 1초씩 순서대로 점등된다. 이 동작이 계속 반복된다.

### 새롭게 알게 된 점

- `pinMode()`로 사용할 디지털 핀을 출력 모드로 설정한다.
- `digitalWrite()`로 LED를 켜거나 끌 수 있다.
- `delay(1000)`은 1초 동안 기다리라는 의미이다.
