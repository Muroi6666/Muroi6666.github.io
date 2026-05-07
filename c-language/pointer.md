# C언어 공부

## 포인터

포인터는 메모리 주소를 저장하는 변수이다.

---

## 예제 코드

```c
#include<stdio.h>

int main()
{
    int a = 10;
    int* p = &a;

    printf("%d\n", *p);

    return 0;
}