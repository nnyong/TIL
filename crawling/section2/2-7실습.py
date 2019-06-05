# 다음 실시간 이슈 검색어 Top10가져오기
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url="https://www.daum.net/"
res=req.urlopen(url).read()
soup=BeautifulSoup(res,"html.parser")
# print(soup.prettify())

top10=soup.select("div.realtime_part>ol.list_hotissue>li>div>div:nth-of-type(1)>span.txt_issue>a")

for i,e in enumerate(top10,1):
    print(i,e.string,e["href"])
