# Day 02

###### 2018.12.18

## Git 설정

* `git config -global user.name 'nnyong'`
* `git config - global user.email 'jo.youthful@gmail.com'`

* `git init`: git 초기화. git으로 관리하겠다.
* `git remote add origin 주소` : 원격 저장소 등록
  * `git remote set -url origin 주소`: 원격 저장소 수정

## Git commit & Push

* `git status`: 현재 폴더의  git의 상태
* `git add .`: 현재 폴더의 변경사항들을 commit하기 위해서 준비
* `git commit -m 'day02입니다.'`: commit, 변경 사항 저장. 메세지는 자유롭게 작성 가능.

* `git push -u origin master`: remote로 등록된 원격 저장소(remote repository)
  * 이후에는 `git push` 만 입력해도 동작합니다.

* Markdown 기록할 것입니다.
  * typora or VSCode
* GitHub Student Developer Pack



## 파일조작



```python
with open('ssafy.txt','w',encoding='utf8') as f:
    f.write('This is SSAFY!, with 이용했다.')
```

encoding은 한글 출력 위함.

```python
import os

os.chdir(r'C:\Users\student\nnyong\day02\dummy')
#print(os.getcwd())
for filename in os.listdir('.'):
    #os.rename(filename,f'지원자_{filename}')

	#합격자_0_이름.txt로 변경
    os.rename(filename,filename.replace('지원자','합격자'))
    #new_filename=filename.replace('지원자','합격자')
    #os.raname(filename,new_filename)
```

getcwd(): 현재 디렉토리 가져오기.