---
layout: default
title: 파이썬 2주차 강의 요약
---

# 파이썬 2주차 강의 요약

## 1. 변수와 자료형

변수는 값을 저장하는 공간이다. 파이썬은 C언어처럼 변수 앞에 자료형을 직접 적지 않아도, 저장되는 값에 따라 자료형이 자동으로 정해진다.

```python
a = 10
b = 10.123

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
```

파이썬에서 자주 사용하는 기본 자료형은 다음과 같다.

- 숫자형: `int`, `float`
- 문자열: `str`
- 리스트: `list`
- 튜플: `tuple`
- 딕셔너리: `dict`
- 집합: `set`
- 불 자료형: `bool`

## 2. 숫자 자료형

정수형 `int`는 음의 정수, `0`, 양의 정수를 표현한다. 실수형 `float`는 소수점을 포함한 숫자를 표현한다.

```python
a = 10       # int
b = 10.123   # float
```

## 3. 연산자

숫자형 자료를 계산할 때 사용하는 기호를 연산자라고 한다.

| 연산자 | 의미 |
| --- | --- |
| `+` | 덧셈 |
| `-` | 뺄셈 |
| `*` | 곱셈 |
| `/` | 나눗셈 |
| `%` | 나머지 |
| `**` | 제곱 |
| `//` | 몫 |

```python
a = 10
b = 5

print(a + b)   # 15
print(a - b)   # 5
print(a * b)   # 50
print(a / b)   # 2.0
print(a % b)   # 0
print(a ** b)  # 100000
print(a // b)  # 2
```

연산자 우선순위는 괄호 `()`, 제곱 `**`, 곱셈/나눗셈/나머지/몫, 덧셈/뺄셈 순서이다.

```python
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20
```

## 4. 복합 연산자

복합 연산자는 산술 연산자와 대입 연산자를 합친 것이다.

```python
a = 10

a = a + 1
a += 1
```

`a += 1`은 `a = a + 1`과 같은 의미이다. 여기서 `=`는 같다라는 뜻이 아니라 오른쪽 값을 왼쪽 변수에 대입한다는 뜻이다.

## 5. 문자열 자료형

문자열은 문자의 모음이다. 따옴표를 사용해 문자열을 만든다.

```python
a = "Hello, world!"
b = 'Python is fun'
c = """여러 줄 문자열"""
d = '''여러 줄 문자열'''
```

문자열 안에 작은따옴표를 넣고 싶으면 큰따옴표로 감싸고, 큰따옴표를 넣고 싶으면 작은따옴표로 감싸면 된다.

```python
a = '누군가 말했다. "최선을 다하라"'
b = "누군가 말했다. '최선을 다하라'"
```

## 6. 사용자 입력 `input()`

`input()` 함수는 사용자에게 값을 입력받을 때 사용한다.

```python
text = input("인사말을 입력하세요: ")
print(text)
```

`input()`으로 입력받은 값은 기본적으로 문자열이다.

## 7. 이스케이프 문자

이스케이프 문자는 문자열 안에서 특수한 의미를 가지는 문자이다. 백슬래시 `\`로 시작한다.

| 이스케이프 문자 | 의미 |
| --- | --- |
| `\n` | 줄바꿈 |
| `\t` | 탭 |
| `\\` | 백슬래시 |
| `\'` | 작은따옴표 |
| `\"` | 큰따옴표 |

```python
print("나랏말씀이\n어쩌고 저쩌고")
print("나랏말씀이\t어쩌고 저쩌고")
```

## 8. 문자열 연산

문자열은 더하기와 곱하기 연산을 사용할 수 있다.

```python
a = "python "
b = "is good"

print(a + b)   # python is good
print(a * 3)   # python python python
```

문자열 더하기는 문자열을 이어 붙이고, 문자열 곱하기는 문자열을 반복한다.

## 9. 문자열 인덱싱과 슬라이싱

인덱싱은 문자열에서 특정 위치의 문자 하나를 가져오는 것이다. 파이썬의 인덱스는 `0`부터 시작한다.

```python
text = "python good"

print(text[0])   # p
print(text[7])   # g
print(text[-1])  # d
```

슬라이싱은 문자열의 일부를 잘라서 가져오는 것이다.

```python
text = "python is good"

print(text[10:14])  # good
print(text[10:])    # good
print(text[:6])     # python
print(text[7:9])    # is
```

슬라이싱의 끝 인덱스에 해당하는 문자는 포함되지 않는다.

## 10. 문자열 관련 함수

| 함수 | 설명 |
| --- | --- |
| `len()` | 문자열 길이 구하기 |
| `count()` | 특정 문자 개수 세기 |
| `upper()` | 대문자로 바꾸기 |
| `lower()` | 소문자로 바꾸기 |
| `strip()` | 양쪽 공백 제거 |
| `lstrip()` | 왼쪽 공백 제거 |
| `rstrip()` | 오른쪽 공백 제거 |
| `split()` | 문자열 나누기 |
| `replace()` | 문자열 바꾸기 |
| `join()` | 문자 사이에 문자열 삽입 |

```python
text = " python is good "

print(len(text))
print(text.count("o"))
print(text.upper())
print(text.lower())
print(text.strip())
print(text.split())
print(text.replace("good", "bad"))
print(",".join("abc"))
```

## 11. 문자열 포맷팅

문자열 포맷팅은 문자열 안에 변수나 값을 넣어 출력하는 방법이다.

```python
print("사과 %d개가 있습니다." % 3)
print("제 이름은 %s입니다." % "김동영")

fruit = "사과"
number = 5
print("저는 %d개의 %s가 있습니다." % (number, fruit))
```

자주 쓰는 포맷 코드는 다음과 같다.

| 코드 | 의미 |
| --- | --- |
| `%s` | 문자열 |
| `%c` | 문자 1개 |
| `%d` | 정수 |
| `%f` | 실수 |
| `%o` | 8진수 |
| `%x` | 16진수 |

헷갈릴 때는 대부분 `%s`를 사용해도 출력할 수 있다.

## 12. 리스트 자료형

리스트는 여러 값을 순서대로 저장하는 자료형이다. 여러 종류의 자료형을 함께 넣을 수 있다.

```python
a = [1, 2, 3]
b = [1, "hello", -1, "hi"]
```

리스트도 문자열처럼 인덱싱과 슬라이싱을 사용할 수 있다.

```python
a = [1, 2, 3, 4, 5]

print(a[0])     # 1
print(a[0:2])   # [1, 2]
```

리스트는 반복, 길이 확인, 수정, 삭제가 가능하다.

```python
a = [1, 2, 3]

print(a * 3)
print(len(a))

a[2] = 4
print(a)  # [1, 2, 4]

del a[1]
print(a)  # [1, 4]
```

## 13. 리스트 관련 함수

| 함수 | 설명 |
| --- | --- |
| `append()` | 리스트 끝에 요소 추가 |
| `sort()` | 리스트 정렬 |
| `reverse()` | 리스트 뒤집기 |
| `index()` | 요소 위치 찾기 |
| `insert()` | 원하는 위치에 요소 삽입 |
| `remove()` | 첫 번째로 나오는 특정 요소 제거 |
| `pop()` | 마지막 요소를 꺼내고 삭제 |
| `count()` | 특정 요소 개수 세기 |

```python
a = [1, 2, 3]
a.append(4)

b = [1, 4, 3, 2]
b.sort()

c = ["a", "c", "b"]
c.reverse()

d = [1, 2, 3]
print(d.index(3))

e = [1, 2, 3]
e.insert(0, 4)

f = [1, 2, 3, 1, 2, 3]
f.remove(3)

g = [1, 2, 3]
g.pop()

h = [1, 2, 3, 1]
print(h.count(1))
```

## 14. 튜플 자료형

튜플은 리스트와 비슷하지만, 한 번 만든 값을 수정하거나 삭제할 수 없다.

```python
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ("a", "b", ("ab", "cd"))
```

요소가 1개인 튜플은 반드시 쉼표를 붙여야 한다.

```python
t = (1,)
```

튜플은 인덱싱, 더하기, 곱하기가 가능하다.

```python
t1 = (1, 2, "a", "b")
print(t1[0])

t2 = (3, 4)
print(t1 + t2)
print(t2 * 3)
```

값이 자주 바뀌어야 하면 리스트를 사용하고, 값이 바뀌면 안 되는 경우에는 튜플을 사용한다.

## 15. 딕셔너리 자료형

딕셔너리는 `Key`와 `Value`를 한 쌍으로 저장하는 자료형이다.

```python
dic = {"사과": "apple", "바나나": "banana", "메론": "melon"}
```

딕셔너리는 순서가 아니라 `Key`를 이용해 `Value`에 접근한다. 그래서 인덱싱과 슬라이싱은 사용할 수 없다.

```python
dic = {1: "one", 2: "two"}

dic[3] = "three"
del dic[2]

print(dic[1])  # one
```

딕셔너리에서 `Key`는 중복될 수 없다. 같은 `Key`를 여러 번 쓰면 마지막 값만 남는다.

```python
test_dic = {1: "one", 2: "two", 2: "둘"}
print(test_dic)  # {1: 'one', 2: '둘'}
```

딕셔너리 관련 함수는 다음과 같다.

```python
dic = {"사과": "apple", "바나나": "banana", "메론": "melon"}

print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get("바나나"))
print("사과" in dic)

dic.clear()
print(dic)
```

## 16. 집합 자료형

집합은 중복을 허용하지 않고, 순서가 없는 자료형이다.

```python
s1 = set([1, 2, 3])
s2 = set("Hello")
s3 = {1, 2, 3}
```

순서가 없기 때문에 인덱싱과 슬라이싱을 사용할 수 없다.

```python
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)           # 교집합
print(s1.intersection(s2))

print(s1 | s2)           # 합집합
print(s1.union(s2))

print(s1 - s2)           # 차집합
print(s1.difference(s2))
```

집합 관련 함수는 다음과 같다.

| 함수 | 설명 |
| --- | --- |
| `add()` | 값 1개 추가 |
| `update()` | 값 여러 개 추가 |
| `remove()` | 특정 값 제거, 없으면 오류 |
| `discard()` | 특정 값 제거, 없어도 오류 없음 |
| `clear()` | 모든 값 제거 |

```python
s = {1, 2, 3}

s.add(4)
s.update([5, 6])
s.remove(2)
s.discard(10)
s.clear()
```

## 17. 불 자료형

불 자료형은 참과 거짓을 표현하는 자료형이다.

```python
True
False
```

불 자료형은 조건식이나 논리 연산자와 자주 사용한다.

| 연산자 | 의미 |
| --- | --- |
| `and` | 양쪽이 모두 참이면 `True` |
| `or` | 둘 중 하나라도 참이면 `True` |
| `not` | 참과 거짓을 반대로 바꿈 |

```python
print(True and True)    # True
print(True and False)   # False

print(True or False)    # True
print(False or False)   # False

print(not True)         # False
print(not False)        # True
```

비교 연산과 함께 사용할 수도 있다.

```python
x = 5
y = 10

print(x > 0 and y > 0)
print(x > 10 or y > 5)
print(not (x > y))
```

## 핵심 정리

- 변수는 값을 저장하는 공간이고, 파이썬은 자료형을 자동으로 판단한다.
- 문자열, 리스트, 튜플은 인덱싱과 슬라이싱을 사용할 수 있다.
- 리스트는 수정 가능하지만, 튜플은 수정할 수 없다.
- 딕셔너리는 `Key`를 이용해 `Value`에 접근한다.
- 집합은 중복을 허용하지 않고 순서가 없다.
- 불 자료형은 조건문과 논리 연산에서 자주 사용한다.
