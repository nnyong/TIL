from bs4 import BeautifulSoup
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# 태그 선택자 이용해 한번에 가져오기
html="""
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

soup=BeautifulSoup(html,'html.parser')

links=soup.find_all("a")
print('links',type(links))
# links <class 'bs4.element.ResultSet'>
a=soup.find_all("a",string="daum")
print('a',a)
# a [<a href="http://www.daum.net">daum</a>, <a href="http://www.daum.com">daum</a>]
b=soup.find("a")
print('b',b)
# b <a href="http://www.naver.com">naver</a> 가장 상위 하나 가져옴.
c=soup.find_all("a",limit=3)
print('c',c)
# c [<a href="http://www.naver.com">naver</a>, <a href="http://www.daum.net">daum</a>, <a href="http://www.daum.com">daum</a>]
d=soup.find_all(string=["naver","google"])
print('d',d)
# d ['naver', 'google'] 해당 내용을 찾아옴. but 보통 이렇게 쓰지 않음.
print('d',type(d))
# d <class 'bs4.element.ResultSet'>

for a in links:
    print('a',type(a),a)
    # a <class 'bs4.element.Tag'> <a href="http://www.naver.com">naver</a>
    # a <class 'bs4.element.Tag'> <a href="http://www.daum.com">daum</a>
    # a <class 'bs4.element.Tag'> <a href="http://www.google.com">google</a>
    # a <class 'bs4.element.Tag'> <a href="http://www.tistory.com">tistory</a>
    href=a.attrs['href']
    # attrs: 속성. href=""에서 href가 key ""가 value
    txt=a.string
    print('txt >> ',txt,'href >> ',href)
    # txt >>  naver href >>  http://www.naver.com
    # txt >>  daum href >>  http://www.daum.com
    # txt >>  google href >>  http://www.google.com
    # txt >>  tistory href >>  http://www.tistory.com
