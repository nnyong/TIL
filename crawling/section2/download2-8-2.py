from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

base="https://www.inflearn.com/"
quote=rep.quote_plus("")
url=base+quote
print(url)

res=req.urlopen(url)
savePath="C:\\imagedown\\" # c:\imagedown\

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
# 권한이 없어서 폴더 만드는 것 실패한 경우
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise #에러 강제로 실행 시킴

soup=BeautifulSoup(res,"html.parser")

img_list=soup.select("ul.slides")[0]

for i,img_list in enumerate(img_list,1):
    with open(savePath+"text_"+str(i)+".txt","wt") as f:
    # wt:text형태로 write하겠다.
        f.write(e.select_one("h4.block_title>a").string)
    fullFileName=os.path.join(savePath,savePath+str(i)+'.png')
    # .png, .jpg 상관 없음.
    req.urlretrieve(e.select_one("div.block_media>a>img")['src'],fullFileName)

print("다운로드 완료")
