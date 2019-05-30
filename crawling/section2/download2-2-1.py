print('hi')
print('안녕') #한글은 깨져서 나옴. anaconda prompt에서는 가능.
#따라 항상 시작 전에 아래 구문 넣기
import sys
import io
import urllib.request as dw

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

print('hi')
print('한글')

imgUrl="https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2F20100113_10%2Fdbwjd177_12633924830421M1mY_jpg%2Fc6f7b8de2_yousongyee_dbwjd177.jpg&type=b360"
htmlURL="http://google.com"

savePath1="c:/test1.jpg"
savePath2="c:/index.html"
# urllib.request.urlretrieve(imgUrl,savePath)
dw.urlretrieve(imgUrl,savePath1)
dw.urlretrieve(htmlURL,savePath2)

print('다운로드 완료!')
# 주로 이미지보다 html파일을 저장해서 필요한 정보를 파싱
# 주기적으로 파싱하는 경우, 원하는 확장자를 지정해 두면 url 통해 다운받을 수 있음. 나중에.
