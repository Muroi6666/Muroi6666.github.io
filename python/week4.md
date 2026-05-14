---
layout: default
title: 파이썬 4주차 강의 요약
---

# 파이썬 4주차 강의 요약

## 1. 파일 입출력이란?

파일 입출력은 파이썬 프로그램에서 파일을 만들거나, 파일에 내용을 쓰거나, 파일의 내용을 읽는 작업이다.

파이썬에서는 `open()` 함수를 사용해 파일을 다룬다.

```python
파일객체 = open("파일이름", "모드")
파일객체.close()
```

파일을 열었다면 작업이 끝난 뒤 `close()`로 닫아 주는 것이 좋다.

## 2. 파일 열기 모드

`open()` 함수의 두 번째 값에는 파일을 어떤 방식으로 열지 지정한다.

| 모드 | 의미 |
| --- | --- |
| `w` | 쓰기 모드. 파일이 없으면 만들고, 있으면 기존 내용을 지운다 |
| `r` | 읽기 모드. 파일을 읽을 때 사용한다 |
| `a` | 추가 모드. 기존 내용 뒤에 새 내용을 추가한다 |

```python
f = open("새파일.txt", "w")
f.close()
```

위 코드는 현재 실행 위치에 `새파일.txt` 파일을 만든다.

특정 폴더에 파일을 만들고 싶으면 경로를 함께 적는다.

```python
f = open("C:/아무거나/새파일.txt", "w")
f.close()
```

## 3. 파일에 내용 쓰기

파일에 문자열 데이터를 쓰려면 `write()` 함수를 사용한다.

```python
f = open("C:/아무거나/새파일.txt", "w")

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close()
```

`\n`은 줄바꿈 문자이다. 파일에 여러 줄을 저장하고 싶을 때 사용한다.

같은 내용을 화면에 출력하면 다음과 같은 흐름이다.

```python
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)
```

## 4. `readline()` 함수

`readline()`은 파일에서 한 줄씩 읽어 오는 함수이다.

```python
f = open("C:/아무거나/새파일.txt", "r")

line = f.readline()
print(line)

f.close()
```

위 코드는 파일의 첫 번째 줄만 읽어서 출력한다.

모든 줄을 한 줄씩 읽으려면 `while`문과 함께 사용할 수 있다.

```python
f = open("C:/아무거나/새파일.txt", "r")

while True:
    line = f.readline()

    if not line:
        break

    print(line)

f.close()
```

`readline()`은 더 이상 읽을 줄이 없으면 빈 문자열을 반환한다. 그래서 `if not line:` 조건으로 반복을 종료할 수 있다.

## 5. `readlines()` 함수

`readlines()`는 파일의 모든 줄을 읽어서 리스트로 반환한다.

```python
f = open("C:/아무거나/새파일.txt", "r")

lines = f.readlines()
print(lines)

f.close()
```

예를 들어 파일에 10줄이 있다면, 각 줄이 리스트의 요소로 들어간다.

```python
[
    "1번째 줄입니다.\n",
    "2번째 줄입니다.\n",
    "3번째 줄입니다.\n"
]
```

`readline()`은 한 줄씩 읽고, `readlines()`는 전체 줄을 리스트로 읽는다는 차이가 있다.

## 6. `with`문으로 파일 다루기

파일을 열고 닫을 때는 `with`문을 사용하면 더 편하다. `with`문을 사용하면 작업이 끝난 뒤 파일이 자동으로 닫힌다.

```python
with open("C:/아무거나/새파일.txt", "w") as f:
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
```

읽을 때도 같은 방식으로 사용할 수 있다.

```python
with open("C:/아무거나/새파일.txt", "r") as f:
    lines = f.readlines()
    print(lines)
```

## 7. API 요청 예제

강의 후반에는 `requests`, `json`, `random` 모듈을 사용해 외부 API에서 데이터를 받아오는 예제가 나온다.

```python
import requests
import json
import random

apikey = "발급받은_API_KEY"
player = input("사용자: ")
query = player[-1]

url = (
    "https://opendict.korean.go.kr/api/search"
    "?certkey_no=인증키번호"
    "&key=" + apikey +
    "&target_type=search"
    "&req_type=json"
    "&part=word"
    "&sort=popular"
    "&start=1"
    "&num=100"
    "&method=start"
    "&pos=1"
    "&q=" + query
)

response = requests.get(url)
words = json.loads(response.text)
```

이 예제의 흐름은 다음과 같다.

1. 사용자에게 단어를 입력받는다.
2. 입력한 단어의 마지막 글자를 가져온다.
3. API 주소를 만들어 요청한다.
4. JSON 형식의 응답을 파이썬 딕셔너리처럼 다룬다.
5. 조건에 맞는 단어를 리스트에 모은다.
6. `random.choice()`로 단어 하나를 골라 출력한다.

```python
list_a = []

for i in range(len(words["channel"]["item"])):
    word = words["channel"]["item"][i]["sense"]["word"]

    if word.startswith(query):
        list_a.append(word.replace("-", "").replace("^", " "))

if len(list_a) > 0:
    print("컴퓨터:", random.choice(list_a))
else:
    print("컴퓨터: 단어 없음")
```

API 키는 외부에 공개하지 않는 것이 좋다. GitHub 같은 공개 저장소에 올릴 때는 실제 키 대신 자리표시자를 사용해야 한다.

## 8. 딕셔너리 값 변경

딕셔너리는 `Key`를 이용해 값을 가져오거나 수정할 수 있다.

```python
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕"],
    "origin": "필리핀"
}

print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
```

값을 바꾸려면 기존 `Key`에 새 값을 대입한다.

```python
dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])
```

딕셔너리는 여러 정보를 `Key: Value` 형태로 묶어 저장할 때 유용하다.

## 핵심 정리

- `open()`은 파일을 열 때 사용하는 함수이다.
- `w` 모드는 쓰기, `r` 모드는 읽기, `a` 모드는 추가 모드이다.
- `write()`는 파일에 문자열을 쓴다.
- `readline()`은 파일을 한 줄씩 읽는다.
- `readlines()`는 파일의 모든 줄을 리스트로 읽는다.
- `with open(...) as f:`를 사용하면 파일을 자동으로 닫을 수 있다.
- `requests.get()`으로 외부 API에 요청을 보낼 수 있다.
- `json.loads()`는 JSON 문자열을 파이썬 자료형으로 바꾼다.
- 딕셔너리는 `Key`를 사용해 값을 읽고 수정한다.
