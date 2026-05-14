---
layout: default
---

# 파이썬 3주차 강의 요약

## 1. 제어문이란?

제어문은 프로그램의 흐름을 제어하는 문장이다. 조건에 따라 실행할 코드를 선택하거나, 같은 코드를 여러 번 반복할 때 사용한다.

파이썬에서 자주 사용하는 제어문은 다음과 같다.

- 조건문: `if`, `elif`, `else`
- 반복문: `while`, `for`
- 반복 흐름 제어: `break`, `continue`

## 2. `if`문

`if`문은 조건이 참일 때만 특정 코드를 실행한다.

```python
if 조건문:
    실행할 문장
```

파이썬에서는 들여쓰기가 매우 중요하다. 같은 `if`문 안에서 실행될 문장들은 들여쓰기 위치가 같아야 한다.

```python
x = 10

if x > 0:
    print("양수입니다.")
```

## 3. 비교 연산자

조건문에서는 값을 비교하기 위해 비교 연산자를 자주 사용한다.

| 연산자 | 의미 |
| --- | --- |
| `x < y` | x가 y보다 작다 |
| `x > y` | x가 y보다 크다 |
| `x == y` | x와 y가 같다 |
| `x != y` | x와 y가 같지 않다 |
| `x >= y` | x가 y보다 크거나 같다 |
| `x <= y` | x가 y보다 작거나 같다 |

```python
x = 3
y = 2

print(x > y)   # True
print(x == y)  # False
print(x != y)  # True
```

## 4. `if`, `elif`, `else`

조건이 여러 개일 때는 `elif`와 `else`를 함께 사용할 수 있다.

```python
if 조건1:
    조건1이 참일 때 실행
elif 조건2:
    조건1은 거짓이고 조건2가 참일 때 실행
else:
    위 조건들이 모두 거짓일 때 실행
```

`elif`는 여러 번 사용할 수 있지만, `else`는 마지막에 한 번만 사용할 수 있다.

```python
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")
```

## 5. 논리 연산자

논리 연산자는 여러 조건을 연결하거나 조건의 참과 거짓을 반대로 바꿀 때 사용한다.

| 연산자 | 의미 |
| --- | --- |
| `and` | 두 조건이 모두 참이면 `True` |
| `or` | 두 조건 중 하나라도 참이면 `True` |
| `not` | 참과 거짓을 반대로 바꿈 |

```python
x = 10
y = 5

print(x > 0 and y > 0)   # True
print(x > 0 or y < 0)    # True
print(not x > y)         # False
```

## 6. `in`, `not in`

`in`과 `not in`은 어떤 값이 리스트, 튜플, 문자열 안에 있는지 확인할 때 사용한다.

```python
print(1 in [1, 2, 3])        # True
print(1 not in [1, 2, 3])    # False
print("a" in "apple")        # True
```

사용 가능한 형태는 다음과 같다.

- `x in 리스트`
- `x not in 리스트`
- `x in 튜플`
- `x not in 튜플`
- `x in 문자열`
- `x not in 문자열`

## 7. `while`문

`while`문은 조건이 참인 동안 코드를 반복 실행한다.

```python
while 조건문:
    실행할 문장
```

```python
jump = 0

while jump < 10:
    jump = jump + 1
    print("점프를 %d번 했습니다." % jump)

    if jump == 10:
        print("점프 10번 성공했습니다.")
```

`while`문에서는 조건이 계속 참이면 반복이 끝나지 않으므로, 반복을 멈출 수 있는 조건을 잘 만들어야 한다.

## 8. `break`

`break`는 반복문을 강제로 빠져나갈 때 사용한다.

```python
coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피는 %d개입니다." % coffee)

    if coffee == 0:
        print("커피가 모두 떨어졌습니다. 판매를 중지합니다.")
        break
```

위 예제는 커피 개수가 `0`이 되면 `break`를 만나 반복문을 종료한다.

## 9. `continue`

`continue`는 반복문을 완전히 끝내지는 않고, 반복문의 처음으로 돌아가 다음 반복을 진행한다.

```python
a = 0

while a < 10:
    a = a + 1

    if a % 2 == 0:
        continue

    print(a)
```

위 코드는 짝수일 때 `continue`를 만나 `print(a)`를 건너뛰기 때문에 홀수만 출력한다.

## 10. 무한 루프

무한 루프는 끝없이 반복되는 반복문이다.

```python
while True:
    실행할 문장
```

`while True`는 조건이 항상 참이기 때문에 직접 멈추지 않으면 계속 실행된다. 보통 `break`와 함께 사용한다.

```python
while True:
    answer = input("종료하려면 q를 입력하세요: ")

    if answer == "q":
        break
```

## 11. `for`문

`for`문은 리스트, 튜플, 문자열 같은 자료형에서 값을 하나씩 꺼내 반복한다.

```python
for 변수 in 리스트 또는 튜플 또는 문자열:
    실행할 문장
```

```python
test_list = ["one", "two", "three"]

for i in test_list:
    print(i)
```

리스트의 값이 순서대로 `i`에 들어가며 반복된다.

## 12. `for`문 활용 예제

학생들의 점수를 리스트로 저장하고, 각 학생의 합격 여부를 출력할 수 있다.

```python
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1

    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
```

반복문 안에서도 `if`문을 함께 사용할 수 있다.

## 13. `for`문과 `continue`

`continue`는 `for`문에서도 사용할 수 있다. 조건에 맞는 경우 현재 반복의 나머지 문장을 건너뛰고 다음 반복으로 넘어간다.

```python
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1

    if mark < 60:
        continue

    print("%d번 학생 축하합니다. 합격입니다." % number)
```

위 코드는 60점 미만 학생은 출력하지 않고 넘어간다.

## 14. `range()` 함수

`range()`는 숫자 범위를 만들어 주는 함수이다. `for`문과 함께 자주 사용한다.

```python
a = range(10)
print(a)  # range(0, 10)
```

`range(10)`은 `0`부터 `10` 미만까지의 숫자를 의미한다.

```python
for i in range(10):
    print(i)
```

시작 숫자와 끝 숫자를 직접 지정할 수도 있다.

```python
for i in range(1, 11):
    print(i)
```

끝 숫자는 포함되지 않는다.

## 15. `range()` 활용 예제

`range()`를 사용해 1부터 10까지의 합을 구할 수 있다.

```python
add = 0

for i in range(1, 11):
    add = add + i

print(add)  # 55
```

`for`문에서도 `break`를 사용해 반복문을 강제로 종료할 수 있다.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

위 코드는 `i`가 `5`가 되면 반복문이 종료되므로 `0`부터 `4`까지만 출력된다.

## 16. 함수

함수는 특정 기능을 수행하는 코드 묶음이다. 필요한 값을 입력받고, 처리한 결과를 반환할 수 있다.

기본 형태는 다음과 같다.

```python
def 함수이름(매개변수):
    실행할 문장
    return 반환값
```

예를 들어 두 수를 더하는 함수는 다음과 같이 만들 수 있다.

```python
def add(a, b):
    result = a + b
    return result

a = add(3, 4)
print(a)  # 7
```

여기서 `a`, `b`는 함수에 전달되는 값이고, `return`은 함수의 결과를 돌려주는 역할을 한다.

## 핵심 정리

- `if`문은 조건에 따라 실행할 코드를 선택한다.
- `elif`는 여러 조건을 추가할 때 사용하고, `else`는 모든 조건이 거짓일 때 실행된다.
- `while`문은 조건이 참인 동안 반복한다.
- `for`문은 리스트, 튜플, 문자열 등의 값을 하나씩 꺼내 반복한다.
- `break`는 반복문을 종료하고, `continue`는 다음 반복으로 넘어간다.
- `range()`는 숫자 범위를 만들어 `for`문에서 자주 사용한다.
- 함수는 반복해서 사용할 기능을 하나로 묶어 놓은 코드이다.
