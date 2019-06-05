from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

base="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote=rep.quote_plus("박보영")
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

img_list=soup.select("div.img_area._item >a.thumb._thumb>img")

for i,img_list in enumerate(img_list,1):
    # print(img_list['data-source'])
    fullFileName=os.path.join(savePath,savePath+str(i)+'.jpg')
    # 폴더에 저장될 이름
    req.urlretrieve(img_list['data-source'],fullFileName)

print("다운로드 완료")
