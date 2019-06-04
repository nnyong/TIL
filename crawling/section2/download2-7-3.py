from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# 인프런 추천강좌 Top10 가져오기
# 현재 홈페이지 변경되어 이 방식으로 가져와지지 않음.
#
# base="https://www.inflearn.com/"
# quote=rep.quote_plus("추천-강좌")
# print(quote)
#
# url=base+quote
# res=req.urlopen(url).read()
# soup=BeautifulSoup(res,"html.parser")
#
# recommend=soup.select("ul.slides")[0]
#
# for i,e in enumerate(recommend,1):
#     print(i,e.select_one("h4.block_title>a"))
