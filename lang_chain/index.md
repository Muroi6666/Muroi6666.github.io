---
layout: default
title: 인공지능프로그래밍 기초 - LangChain
---

# 인공지능프로그래밍 기초 - LangChain

`lang_chain` 폴더는 **인공지능프로그래밍 기초** 과목에서 배운 LangChain 기반 문서 질의응답 실습을 정리하는 공간입니다.

## 학습 주제

- LangChain을 활용한 LLM 애플리케이션 구성
- PDF, TXT, DOCX 문서 불러오기
- 문서를 작은 단위로 나누는 text splitting
- FAISS 벡터스토어를 이용한 문서 검색
- Gemini 모델을 연결한 RAG 문서 기반 챗봇
- 검색된 문맥을 바탕으로 한글 답변 생성

## 폴더 구성

| 파일/폴더 | 설명 |
| --- | --- |
| `langchain.py` | LangChain 문서 기반 챗봇 예제 코드 |
| `requirements.txt` | 실행에 필요한 Python 패키지 목록 |
| `.env.example` | API 키 환경변수 설정 예시 파일 |
| `data/` | 챗봇이 참고할 PDF, TXT, DOCX 자료 저장 폴더 |
| `data-20260528T021220Z-3-001.zip` | 실습 자료 압축 파일 |

## 핵심 개념 정리

### 1. 문서 로딩

`PyPDFLoader`, `TextLoader`, `UnstructuredWordDocumentLoader`를 사용해 PDF, TXT, DOCX 파일을 읽습니다.

문서 파일은 `data` 폴더에 넣고, 확장자에 따라 알맞은 로더를 선택합니다.

### 2. 문서 분할

`RecursiveCharacterTextSplitter`를 사용해 긴 문서를 일정한 크기의 청크로 나눕니다.

문서를 잘게 나누면 질문과 관련 있는 부분만 검색하기 쉬워지고, LLM에 전달할 문맥도 더 깔끔해집니다.

### 3. 임베딩과 벡터스토어

예제 코드에서는 `HashingVectorizer` 기반의 로컬 임베딩 클래스를 만들어 사용합니다.

생성된 문서 청크는 FAISS 벡터스토어에 저장하고, 질문이 들어오면 관련 문서를 검색합니다.

### 4. RAG 질의응답

RAG는 Retrieval-Augmented Generation의 약자로, 문서를 먼저 검색한 뒤 검색 결과를 LLM 답변 생성에 함께 사용하는 방식입니다.

이 실습에서는 다음 흐름으로 동작합니다.

1. 사용자가 질문을 입력한다.
2. FAISS retriever가 관련 문서 청크를 찾는다.
3. 검색된 문맥과 질문을 prompt에 넣는다.
4. Gemini 모델이 문맥을 근거로 한글 답변을 생성한다.

## 실행 방법

```bash
cd lang_chain
pip install -r requirements.txt
$env:GOOGLE_API_KEY="내_구글_API_키"
python langchain.py
```

실행 후 질문을 입력하면 `data` 폴더에 있는 문서를 바탕으로 답변을 생성합니다.

API 키는 코드에 직접 적지 않고 `GOOGLE_API_KEY` 환경변수로 설정해서 사용합니다.

종료하려면 `q`, `quit`, `exit`, `종료` 중 하나를 입력합니다.

## 예제 질문

- 금융기관에 대해서 분류해줘.
- 주택 임대시 주의점은 무엇인가요?

## 복습 포인트

- LLM은 스스로 문서를 읽는 것이 아니라, 검색된 문맥을 prompt로 전달받아 답변한다.
- RAG에서는 문서 로딩, 청크 분할, 임베딩, 검색, 답변 생성 단계가 중요하다.
- 벡터스토어는 질문과 의미가 비슷한 문서 조각을 빠르게 찾기 위해 사용한다.
- prompt에 답변 규칙을 명확히 적으면 원하는 형식의 답변을 얻기 쉽다.
