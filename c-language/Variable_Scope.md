---
layout: default
title: C언어 변수 사용 영역
---

# C언어 공부

## 변수 사용 영역

변수는 선언 위치와 방법에 다라 다양한 특징을 가집니다.
변수의 특징을 이해하고 필요한 곳에 적재적소로 사용하면 메모리를 절약할 수 있고 신뢰성있는 코드를 만들 수 있습니다.

크게 

- `지역 변수(Local Variable)`
- `전역 변수(Global Variable)`
- `정적 변수(Static Variable)`
- `레지스터 변수(Register Variable)`

로 나뉘어집니다.

---
### 지역 변수

우리가 평소에 배우던 변수는 모두 지역 변수(local variable)입니다. 지역 변수는 범위가 함수 내, 즉 일정 지역에서만 사용하는 변수입니다. "auto"라는 예약어와 함께 사용하여 지역변수를 선언합니다. "auto" 예약어는 생략이 가능

### 예제 코드

```c
#include<stdio.h>

void sum(void);

int main()
{
    auto int a = 0;
    sum();
    printf("main함수 a : %d\n", a);
}

void sum(void)
{
    int a = 0;
    int b = 5;

    a = a + b;

    printf("sum함수 a : %d\n", a);

}
```


---

### 실행 결과

```text
sum함수 a : 5
main함수 a : 0
```

---

### 설명

- `main()` 함수의 `a`와 `sum()` 함수의 `a`는 서로 다른 지역 변수이다.
- 지역 변수는 선언된 함수 내부에서만 사용할 수 있다.
- 함수가 종료되면 지역 변수는 메모리에서 제거된다.
