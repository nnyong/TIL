#  TIL

## Day 01

### github 가입

#### 조영현

##### 2018.12.18

###### 안녕:)



* 앞으로 실습 코드 올라가는 곳
  https://github.com/sgmpy

* $ git init 
  $ git config --global --list 확인용
  $ git config --global user.name 'nnyong'
  $ git config --global user.email 'jo.youthful@gmail.com'
  $ git status //상태 확인
  $ git add day01/money.py
  $ git add . //현재 폴더 모든 파일들.
  $ git commit -m 'first commit' //잘 알아볼 수 있는 이름으로 설정.
  $ git remote add origin https://github.com/nnyong/TIL.git 
  $ git remote -v
  origin  https://github.com/nnyong/TIL.git (fetch) 내려받는 것
  origin  https://github.com/nnyong/TIL.git (push) 업로드하는 것
  $ git push origin master
  //로그인 창 뜸.

  `$ git push -u origin master                                        `

* https://typora.io/

* https://guides.github.com/features/mastering-markdown/  문서 작성 가이드
* https://education.github.com/pack 학생에게 2년동안 무료로  github에서 제공해주는 것. 학교 이메일로 인증



```python
import requests

response='응답'
#123123
```

* 오른쪽 마우스 -> 추가 -> 삽입 -> 코드 펜스
* 원하는 언어 오른쪽 아래에 적어주기 ex) python, bash 등

```bash
git confit --global user.name 'nnyong'
```



### vscode 기본 terminal 변경

* `ctrl+shift+p`
* shell 검색
* Select Default Shell
* Git Bash



### vscode 단축키

* ctrl+` : 터미널 창 띄우기
* clear 입력 대신 ctrl+ L 사용 가능



### 파일명 변경

1. `os.chdir(r'폴더 주소')`
2. `os.listdir('.')` 현재 working directory의 파일 목록 리스트로
3. `os.random('바꾸고자하는 이름', '바꿀 이름')`







