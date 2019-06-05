# 네이버 실시간 이슈 검색어 Top20가져오기
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url="https://www.naver.com/"
res=req.urlopen(url).read()
soup=BeautifulSoup(res,"html.parser")
# print(soup.prettify())

top10=soup.select("div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a.ah_a")
# print(top10)

for i,e in enumerate(top10,1):
    print(i,e.select("span.ah_k")[0].string, e['href'])
