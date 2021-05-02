[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![python](https://img.shields.io/badge/Python-3.8.8-1f425f)](https://www.python.org/)
[![django](https://img.shields.io/badge/django-3.2-092e20)](https://www.djangoproject.com/)

# HelloBot Clone API 가이드

[TOc]

## Tools

> pyenv == 1.2.26
>
> sqlite3 == 3.32.3
>
> vscode == 1.55.1
>
> macOS == 11.2.3

<br>

## Guide

1. git clone

   ```bash
   $ git clone https://github.com/withyeah/HelloBot-Clone.git
   ```

2. 가상환경 생성 및 실행

   ```bash
   $ python -m venv venv
   
   # macOS
   $ source venv/bin/activate
   
   # windows
   $ source venv/Scripts/activate
   ```

3. 패키지 설치

   ```bash
   $ pip install -r requirements.txt
   ```

4. run server

   ```bash
   $ python manage.py runserver
   ```

<br>

## API SWAGGER

> http://127.0.0.1:8000/api/v1/swagger/
>
> ![api_swagger](https://user-images.githubusercontent.com/45819975/116817789-14af8c00-aba3-11eb-8457-73865ccd59a2.png)

### 1. Scenario

**챗봇과의 대화 구현 및 사용을 위한 API**

1. GET /scenarios/ : 전체 시나리오 리스트 Read

2. POST /scenarios/ : 시나리오 Create

   예시) {'input_message': '오늘의 썸 연애운',

   ​          'output_message': '설레지만 애매하고 답답한 우리 사이...\n/images/1\n오늘의 썸 연애운을 타로 카드로 확인해보자',

   ​          'next_question': '썸상대를 뭐라고 부르면 좋은지 말해줘'}

   `참고`) output_message 처럼 메세지가 길어지거나 선택지를 제공할 때는 `\n`으로 구분하여 추후 잘라서 사용

3. GET, PUT, PATCH, DELETE /scenarios/{id}/ : 개별 시나리오 Read, Create, Update, Partial Update, Delete

<br>

### 2. Tarot

**타로 카드 해설 구현 및 사용을 위한 API**

1. GET /tarots/ : 전체 타로 해설 리스트 Read

2. POST /tarots/ : 타로 카드 해설 Create

   예시) {'card_number': 1,

   ​          'card_image': 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==',

   ​          'explanation': '오.. 농작물을 바라보고 사람이 서있어\n/images/emoticon/2\n나는 고백을 추천한다'}

3. GET, PUT, PATCH, DELETE /tarots/{id}/ : 개별 타로 카드 해설 Read, Create, Update, Partial Update, Delete

<br>

## Testing

- 테스트 파일 위치 : /chats/tests/

- 테스트 방법

  ```bash
  $ python manage.py test
  ```

  

