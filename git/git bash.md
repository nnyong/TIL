###### 190510

#### git bash에서 python툴 쓰기

```bash
cd ~
code .bash_profile
```

* bash_profile

  ```
  alias python='winpty python'
  ```

다시 돌아가서

```bash
python
```

=> python shell 열림.



* 가상환경 설정

  ```bash
  python -m venv api-venv
  ls //확인해보렴
  source api-venv/Scripts/activate
  ```

  but, 버전 안맞으면 안됨!

  그럴때는 cmd를 켜장!



##### cmd

```bash
api-venv\Scripts\activate
// 가상환경 활성화
pip install django
django-admin startproject api .
python manage.py runserver
```

뜨는 주소(ex) http://xxx.x.x.x:8000/)로 접속해도 되고 아니면, http://localhost:8000/로 접속



##### cmd대신 visual Studio Code에서 cmd창 열어서 해도 됨.

* ctrl+shift+P

  > shell
  >
  > commend prompt 실행

  ctrl+`

```bash
python -m venv api-venv
api-venv\Scripts\activate
pip install django==2.1.8
pip install djangorestframework
pip install django-rest-swagger
python manage.py runserver
```







