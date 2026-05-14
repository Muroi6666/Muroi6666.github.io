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

#### 지역 변수 특징

- 지역 변수는 사용 범위가 블록 내부로 제한되므로 다른 함수에서는 사용할 수 없습니다.
- 지역 변수는 이름이 같아도 선언된 함수가 다르면 각각 독립된 저장 공간을 갖습니다.

#### 지역 변수 장점
- 메모리를 효율적으로 사용
- 디버깅에 유리

---

#### 블록 안에서 사용하는 지역 변수 예제코드
```c
#include<stdio.h>

int main(void)
{
    int a = 10, b = 20;

    printf("교환 전 a와 b의 값 : %d, %d\n", a, b);
    {
        int imsi;

        imsi = a;
        a = b;
        b = imsi;
    }
    printf("교환 후 a와 b의 값 : %d, %d\n", a, b);

    return 0;
}

```

#### 설명

- 지역 변수는 보통 함수 안에서 선언한 후 함수 끝까지 사용하지만 선언 위치에 따라 사용 범위가 달라질 수 있습니다.
- 지금 사용하고 있는 main또한 main()함수입니다.

---
### 전역 변수

전역 변수(global variable)는 함수 밖에서 선언하는 변수입니다. 특정 함수 안에서만 사용하는 것이 아니라 여러 함수에서 함께 사용할 수 있습니다.

전역 변수는 프로그램이 시작될 때 메모리에 만들어지고, 프로그램이 끝날 때까지 유지됩니다.

### 예제 코드

```c
#include <stdio.h>

int count = 0;  // 전역 변수

void increase(void);

int main(void)
{
    printf("main 함수 시작 count : %d\n", count);

    increase();
    increase();

    printf("main 함수 종료 count : %d\n", count);

    return 0;
}

void increase(void)
{
    count++;
    printf("increase 함수 count : %d\n", count);
}
```

### 실행 결과

```text
main 함수 시작 count : 0
increase 함수 count : 1
increase 함수 count : 2
main 함수 종료 count : 2
```

### 설명

- `count`는 함수 밖에서 선언되었으므로 전역 변수입니다.
- `main()` 함수와 `increase()` 함수가 같은 `count`를 공유합니다.
- 전역 변수는 여러 함수에서 접근할 수 있어 편리하지만, 값이 어디서 바뀌었는지 추적하기 어려울 수 있습니다.

---

### 정적 변수

정적 변수(static variable)는 `static` 예약어를 사용해 선언하는 변수입니다. 함수 안에서 선언하면 지역 변수처럼 해당 함수 안에서만 사용할 수 있지만, 함수가 끝나도 값이 사라지지 않습니다.

즉, 사용 범위는 지역 변수처럼 좁고 값의 수명은 전역 변수처럼 깁니다.

### 예제 코드

```c
#include <stdio.h>

void visit(void);

int main(void)
{
    visit();
    visit();
    visit();

    return 0;
}

void visit(void)
{
    static int count = 0;  // 정적 지역 변수

    count++;
    printf("visit 함수 호출 횟수 : %d\n", count);
}
```

### 실행 결과

```text
visit 함수 호출 횟수 : 1
visit 함수 호출 횟수 : 2
visit 함수 호출 횟수 : 3
```

### 설명

- `count`는 `visit()` 함수 안에서 선언되었기 때문에 함수 밖에서는 사용할 수 없습니다.
- 하지만 `static`이 붙었기 때문에 `visit()` 함수가 끝나도 값이 유지됩니다.
- 함수를 호출할 때마다 `count`가 다시 `0`이 되는 것이 아니라 이전 값을 기억합니다.

---

### 레지스터 변수

레지스터 변수(register variable)는 `register` 예약어를 사용해 선언하는 변수입니다. CPU의 레지스터처럼 빠른 저장 공간에 저장해 달라고 컴파일러에 요청하는 의미입니다.

다만 실제로 레지스터에 저장할지는 컴파일러가 결정합니다. 요즘 컴파일러는 최적화를 잘하기 때문에 직접 `register`를 사용하는 경우는 많지 않습니다.

### 예제 코드

```c
#include <stdio.h>

int main(void)
{
    register int i;
    int sum = 0;

    for (i = 1; i <= 5; i++)
    {
        sum = sum + i;
    }

    printf("1부터 5까지의 합 : %d\n", sum);

    return 0;
}
```

### 실행 결과

```text
1부터 5까지의 합 : 15
```

### 설명

- `register int i;`는 `i`를 빠르게 접근할 수 있는 저장 공간에 두도록 요청하는 코드입니다.
- 반복문에서 자주 사용하는 변수에 사용할 수 있습니다.
- 레지스터 변수에는 주소 연산자 `&`를 사용할 수 없습니다.

```c
register int i = 10;
printf("%p\n", &i);  // 오류가 발생할 수 있음
```

---

## 핵심 정리

| 종류 | 선언 위치 | 사용 범위 | 값 유지 |
| --- | --- | --- | --- |
| 지역 변수 | 함수 또는 블록 내부 | 선언된 함수/블록 내부 | 함수나 블록이 끝나면 사라짐 |
| 전역 변수 | 함수 외부 | 여러 함수에서 사용 가능 | 프로그램 종료까지 유지 |
| 정적 변수 | 함수 내부 또는 함수 외부 | 선언 위치에 따라 다름 | 프로그램 종료까지 유지 |
| 레지스터 변수 | 함수 또는 블록 내부 | 선언된 함수/블록 내부 | 일반 지역 변수와 비슷함 |

특별한 이유가 없다면 지역 변수를 우선 사용하는 것이 좋습니다. 여러 함수가 함께 사용해야 하는 값은 전역 변수로 둘 수 있고, 함수 안에서만 쓰지만 값을 계속 기억해야 한다면 정적 변수를 사용할 수 있습니다.

