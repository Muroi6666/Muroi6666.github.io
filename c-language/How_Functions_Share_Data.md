---
layout: default
title: C언어 함수 사이의 데이터 공유
---

# 함수 사이의 데이터 공유

C언어에서 함수는 서로 데이터를 주고받으며 동작한다. 데이터를 전달하는 대표적인 방법은 다음 세 가지이다.

- 값을 복사해서 전달
- 주소를 전달
- 주소를 반환

---

## 1. 값을 복사해서 전달

함수에 변수를 전달하면 변수의 실제 값이 복사되어 매개변수로 들어간다. 함수 안에서 매개변수를 바꾸어도 원래 변수는 바뀌지 않는다.

### 예제 코드

```c
#include <stdio.h>

void changeValue(int num);

int main(void)
{
    int a = 10;

    printf("changeValue 호출 전 a: %d\n", a);
    changeValue(a);
    printf("changeValue 호출 후 a: %d\n", a);

    return 0;
}

void changeValue(int num)
{
    num = 20;
    printf("changeValue 함수 안 num: %d\n", num);
}
```

### 실행 결과

```text
changeValue 호출 전 a: 10
changeValue 함수 안 num: 20
changeValue 호출 후 a: 10
```

### 설명

- `changeValue(a)`를 호출하면 `a`의 값 `10`이 `num`으로 복사된다.
- 함수 안에서 `num`을 `20`으로 바꾸어도 `a`는 그대로 `10`이다.
- 원본 값을 보호하고 싶을 때 유용하다.

---

## 2. 주소를 전달

변수의 주소를 함수에 전달하면 함수 안에서 원래 변수의 값을 직접 바꿀 수 있다. 포인터를 사용한다.

### 예제 코드

```c
#include <stdio.h>

void changeValue(int* num);

int main(void)
{
    int a = 10;

    printf("changeValue 호출 전 a: %d\n", a);
    changeValue(&a);
    printf("changeValue 호출 후 a: %d\n", a);

    return 0;
}

void changeValue(int* num)
{
    *num = 20;
    printf("changeValue 함수 안 *num: %d\n", *num);
}
```

### 실행 결과

```text
changeValue 호출 전 a: 10
changeValue 함수 안 *num: 20
changeValue 호출 후 a: 20
```

### 설명

- `&a`는 변수 `a`의 주소이다.
- `int* num`은 정수형 변수의 주소를 저장하는 포인터이다.
- `*num = 20;`은 `num`이 가리키는 실제 변수 `a`의 값을 바꾼다.
- 함수에서 여러 값을 바꾸거나 원본 데이터를 수정해야 할 때 사용한다.

---

## 3. 주소를 반환

함수가 값이 아니라 주소를 반환할 수도 있다. 이때 반환하는 주소는 함수가 끝난 뒤에도 유효해야 한다.

지역 변수의 주소를 반환하면 안 된다. 지역 변수는 함수가 끝나면 사라지기 때문이다.

### 예제 코드

```c
#include <stdio.h>

int* getNumberAddress(void);

int main(void)
{
    int* p = getNumberAddress();

    printf("반환받은 주소의 값: %d\n", *p);

    *p = 200;
    printf("값 변경 후: %d\n", *p);

    return 0;
}

int* getNumberAddress(void)
{
    static int number = 100;

    return &number;
}
```

### 실행 결과

```text
반환받은 주소의 값: 100
값 변경 후: 200
```

### 설명

- `getNumberAddress()`는 `int*` 자료형을 반환한다.
- `static int number`는 함수가 끝나도 사라지지 않는다.
- 그래서 `&number`를 반환해도 `main()`에서 안전하게 사용할 수 있다.
- 일반 지역 변수의 주소를 반환하면 위험하다.

```c
int* wrongFunction(void)
{
    int number = 100;
    return &number;  // 잘못된 코드
}
```

위 코드에서 `number`는 함수가 끝나면 사라진다. 사라진 변수의 주소를 사용하면 예측할 수 없는 문제가 생긴다.

---

## 핵심 정리

| 방식 | 함수 안에서 원본 변경 | 사용 방법 |
| --- | --- | --- |
| 값을 복사해서 전달 | 불가능 | `changeValue(a)` |
| 주소를 전달 | 가능 | `changeValue(&a)` |
| 주소를 반환 | 가능하지만 주의 필요 | `int* p = getNumberAddress()` |

값을 복사해서 전달하면 안전하지만 원본을 바꿀 수 없다. 주소를 전달하면 원본을 바꿀 수 있지만 포인터를 정확히 사용해야 한다. 주소를 반환할 때는 함수가 끝난 뒤에도 살아 있는 변수의 주소만 반환해야 한다.
