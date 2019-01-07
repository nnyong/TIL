# Git & GitHub

## Git에 내 정보 설정

* `$ git config --global user.name 'nnyong'                                        `: 이름 설정
* `$ git config --global user.email 'jo.youthful@gmail.com'                         `: 이메일 설정
* 

# 자리 바꿀 때 git bash 설정

##### 190107

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



