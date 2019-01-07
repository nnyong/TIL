# Git & GitHub

##### 190107

## Git에 내 정보 설정

- `$ git config --global user.name 'nnyong'                                        `: 이름 설정
- `$ git config --global user.email 'jo.youthful@gmail.com'                         `: 이메일 설정
- `git config --global --list`: 정보 설정 확인



## Git repository를 처음 생성한 경우

* `git init`: git 초기화. 지금 폴더를 git으로 관리하겠다.

  (관리하려는 폴더 안에서 입력)

* `git remote add origin 주소`: 원격 저장소(remote repository) 주소 등록

  * `git remote set-url origin 주소:`: 원격 저장소 수정(주소 잘못 입력했거나 수정할 때)


## Git repository clone한 경우

* `git clone 주소 [폴더 이름]`: 이 주소로부터 내용 내려받기
  * 이 경우에는`git init`, `git remote add origin 주소`를 하지 않아도 이미 다 되어있다.



## Git Commit&Push

* `git status`: 현재 폴더의 git의 상태 확인

* `git add .`: 현재 폴더의 변경사항들을 commit하기 위하여 준비.

  `.` 대신에 특정 파일 이름도 가능.

* `git commit -m 'D04 | 190107 AM | Git & CLI'`: 

  commit, 변경 사항 저장. `''`안에 있는 메세지는 자유롭게 작성 가능

* `git push -u origin master`:remote로 등록된 원격 저장소에 commit한 것들 올리기

  * 이 후에는 `git push`만 입력해도 동작합니다. `git clone`을 한 경우에도 해당합니다.
  * 이 컴퓨터에서 최초 push인 경우, 로그인 창이 뜨며 로그인을 해줍니다.


## Git Pull

* `git pull`: GitHub에 올라가 있는 내용들, 즉 commit들을 내려받는 것.
* 아침에 오자마자 `git pull`한번 하고 시작합시다!



## 자리 바꿀 때 Git & GitHub 재설정

```bash
# Git 이름, 이메일 재설정
git config --global user.name 'nnyong'
git config --global user.email 'jo.youthful@gmail.com'

# GitHub 로그인 정보 초기화
git credential reject
protocol=https
host=github.com
```



* github 페이지 원하는 repository -> Cone or download

  주의: https://로 시작하는지 꼭 확인!

* `$ git clone https://github.com/nnyong/TIL.git nnyong`

  git clone 클론 주소 폴더명

* `$ git credential reject                                                         
  protocol=https                                                                  
  host=github.com                                                                 `

  `$ git push                                                                      `

  기존 로그인 정보 지우고 새로 로그인 하기

* `$ git config --global --list                                                    `

  확인하면 기존 name, email 정보 볼 수 있음.

* `$ git config --global user.name 'nnyong'                                        `

* `$ git config --global user.email 'jo.youthful@gmail.com'                         `

  내껄루 바꾸기

* `$ git log`

  그 동안 남겼던 기록 볼 수 있음

* 기존 자리 주인 폴더에 파일을 commit 하면 commit 까지는 가능. 

  but, `git push` 불가능. 업로드 불가.



