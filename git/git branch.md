### Git branch 사용법

* git branch 만들기

  ``git checkout -b [브랜치명] (develop)``

  develop 추가하면 develop 기준으로 새로운 브랜치 만듬

  ``git push origin [브랜치명]``

  * 새로 만든 branch 작업을 다른 컴퓨터에서 이어가기 위해서는 간단하게 ``git checkout [브랜치명]``하면 됨.



* branch 이름 변경

  ``git branch -m [옛날 이름] [새로운 이름]`` (local에 있는 branch 이름 변경)

  ``git push origin :[옛날이름]`` (remote에 존재하는 예전 branch 삭제)

  ``git push origin [새로운 이름]``(새로운 branch push)



* 브랜치 local에서 삭제

  ``git checkout [상위 브랜치]``

  ``git branch --delete [브랜치명]``

  * 강제로 삭제해야하는 경우

    ``git branch -D [브랜치명]``

    

* 특정 branch clone

  ``git clone -b [브랜치명] [브랜치주소]``



* .gitignore 생성

  * 무시해야할 파일 이미 push한 경우

    .gitignore 파일 생성 후, 해당 파일 설정

    ``git rm -r --cached .``

    ``git add .``

    

    