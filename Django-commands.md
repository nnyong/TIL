* 준비(c9에 python 설치하기)

* https://gist.github.com/nwith

  install_pyenv.sh 복붙

  ```bash
  pyenv install 3.6.7
  pyenv global 3.6.7
  python -V
  ```


### 1. Django

1. 폴더생성

   ```bash
   mkdir [프로젝트 이름]
   cd [프로젝트 이름]
   ```


2. 가상환경 생성

   * 가상환경 생성

     ```BASH
     pyenv virtualenv 3.6.7 [가상환경 이름]
     ```

   * 가상환경 삭제

     ```bash
     pyenv uninstall [가상환경 이름]
     ```

   * 가상환경 목록

     ```bash
     pyenv versions
     ```

   * 현재 폴더에 가상환경 활성화

     ```bash
     pyenv local [가상환경 이름]
     ```

   * 현재 폴더에 활성화된 가상 환경 비활성화

     * `.python-version`파일을 찾아 삭제한다.



### 2. django 프로젝트

* django 설치

  ```bash
  pip install django
  ```

* startproject

  ```bash
  django-admin startproject [프로젝트 이름] .
  ```

* startapp

  ```bash
  python manage.py startapp [앱 이름]
  ```



* django 실행

  ```
  python manage.py runserver $IP:$PORT
  ```



* setting 설정

  ```
  ALLOWED_HOSTS = ['playground-nnyong.c9users.io']
  
  INSTALLED_APPS = [
  		...
      'posts.apps.PostsConfig'
  ]
  
  LANGUAGE_CODE = 'ko-kr'
  
  TIME_ZONE = 'Asia/Seoul'
  
  ```




### CRUD

* posts내에 urls.py 생성

* 기존 url.py 다음과 같이 설정

  ```
  from django.contrib import admin
  from django.urls import path,include
  from posts import views
  
  urlpatterns = [
      path('posts/',include('posts.urls')),
      path('admin/', admin.site.urls),
  ]
  ```

* models 설정

  ```
  class Post(models.Model):
      title=models.CharField(max_length=100)
      content=models.TextField()
  ```

* Migration

  * make migration

    ```
    python manage.py makemigrations
    ```

  * db적용

    ```
    python manage.py migrate
    ```

    * 모델 재설정 하면 migration 다시 해주어야 함.

* 계정 설정

  ```
  python manage.py createsuperuser
  ```

* base.html 추가 시, setting.py에

  ```python
  'DIRS': [os.path.join(BASE_DIR,'[프로젝트이름]','templates')],
  ```

  