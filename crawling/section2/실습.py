import sys
import io
import urllib.request as dw

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

htmlurl="https://www.naver.com/"

imgUrl1="https://ssl.pstatic.net/tveta/libs/1236/1236372/66ad609cf9603878a969_20190524165959472_1.png"
imgUrl2="https://ssl.pstatic.net/tveta/libs/1241/1241486/7a3f4c8c6a51a17069e3_20190524155055182_1.jpg"
# 비디오인 경우
videoUrl="https://tvetamovie.pstatic.net/libs/1234/1234602/f1ad54b90c222ad69717_20190423142816375.mp4-pBASE-v0-f79511-20190423153829544.mp4"

savePath1="c:/add1.jpg"
savePath2="c:/add2.jpg"
savePath3="c:/add2_video.mp4"

dw.urlretrieve(imgUrl1,savePath1)
dw.urlretrieve(imgUrl2,savePath2)
dw.urlretrieve(videoUrl,savePath3)

print('다운로드 완료!')
# 주로 이미지보다 html파일을 저장해서 필요한 정보를 파싱
# 주기적으로 파싱하는 경우, 원하는 확장자를 지정해 두면 url 통해 다운받을 수 있음. 나중에.
