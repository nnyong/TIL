import sys
import io
import urllib.request as dw

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

imgUrl="https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2F20100113_10%2Fdbwjd177_12633924830421M1mY_jpg%2Fc6f7b8de2_yousongyee_dbwjd177.jpg&type=b360"
htmlURL="http://google.com"

savePath1="c:/test1.jpg"
savePath2="c:/index.html"

f=dw.urlopen(imgUrl).read() #이미지 데이터를 f에 할당
f2=dw.urlopen(htmlURL).read()

saveFile1=open(savePath1,'wb') # w:write, r:read, a: add, b:binary
saveFile1.write(f) # f데이터를 쓰겠다.
saveFile1.close()
# 위 세 줄 버전보다
with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)
# 이 두 줄 버전이 더 편함. python 2.x부터 나옴. 옛날 코드에는 위처럼 쓰여있을 수 있음.

print('다운로드 완료!')
