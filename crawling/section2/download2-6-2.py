from bs4 import BeautifulSoup
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

fp=open('food-list.html',encoding='utf-8')
soup=BeautifulSoup(fp,"html.parser")

print("1", soup.select("li:nth-of-type(4)")[1].string)
#각 li 태그 그룹의 4번째 요소 선택
print("2",soup.select_one("#ac-list > li:nth-of-type(4)").string)
# 2 양주
print("3",soup.select("#ac-list > li[data-lo='cn']")[0].string)
# 3 양주
print("4",soup.select("#ac-list > li.alcohol.high")[0].string)
# 클래스 2개인 경우 .으로 연결
# 4 양주

param={"data-lo":"cn","class":"alcohol"}
print("5",soup.find("li",param).string)
# 딕셔너리형태도 들어갈 수 있다.
# 5 양주
print("6",soup.find(id="ac-list").find("li",param).string)
# 이렇게 하면 정확하게 접근을 한 것이지만 5번째 방법이 더 가독성, 효율성이 좋음.
# 6 양주

for ac in soup.find_all("li"):
    if ac['data-lo']=='us':
        print('data-lo==us',ac.string)
        # data-lo==us 스테이크
        # data-lo==us 맥주

# 가져오는 방법만 다를 뿐이지, 궁극적으로 가져 올 값은 같음.
# 방법은 스스로 하는 것에 따라 다름.
