### Git branch 사용법

* git branch 만들기

  ```git branch [브랜치명]```

  ```git checkout [브랜치명] ```(브랜치 이동)

  ```git commit```

  or

  ``git checkout -b [브랜치명] (develop)``

  develop 추가하면 develop 기준으로 새로운 브랜치 만듬

* 브랜치 local에서 삭제

  ``git checkout [상위 브랜치]``

  ``git branch --delete [브랜치명]``

* 특정 branch clone

  ``git clone -b [브랜치명] [브랜치주소]``



* .gitignore 생성

  * 무시해야할 파일 이미 push한 경우

    .gitignore 파일 생성 후, 해당 파일 설정

    ``git rm -r --cached .``

    ``git add .``

    

    