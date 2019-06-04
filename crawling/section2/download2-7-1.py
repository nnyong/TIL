from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# 다음 사이트 수정으로 아래 코드 실행 불가
# 
# url="http://finance.daum.net/"
# res=req.urlopen(url).read()
# soup=BeautifulSoup(res,"html.parser")
#
# # print('soup',soup.prettify())
# # .prettify() 이쁘게 보여주기 위해
#
# top=soup.select("ul#topMyListNo1 > li")
#
# for i,e in enumerate(top,1):
#     (top,1) 시작 인덱스 1로 지정.
#     print(i,",",e.find("a").string," : ", e.find("span").string)
