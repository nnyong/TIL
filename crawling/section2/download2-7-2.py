from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# 네이버 상한가 top4가져오기

url="https://finance.naver.com/"
res=req.urlopen(url).read().decode('cp949')
# utf-8 : 한글 깨짐, unicode_escape : 한글 깨짐
soup=BeautifulSoup(res,"html.parser")

# print(soup)

top4=soup.select("tbody#_topItems1 > tr")

i=1
for e in top4:
    if e.find("a") is not None:
        print(i,e.select_one("a").string)
        i+=1
