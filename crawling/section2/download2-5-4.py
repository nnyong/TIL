# css 선택자 이용해서 조건에 맞는 element 가져오기
# 실제 scraping에서 가장 많이 쓰임.

from bs4 import BeautifulSoup
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

html="""
<html><body>
<div id="main">
    <h1>강의목록</h1>
    <ul class="lecs">
        <li>Java 초고수 되기</li>
        <li>파이썬 기초 프로그래밍</li>
        <li>파이썬 머신러닝 프로그래밍</li>
        <li>안드로이드 블루투스 프로그래밍</li>
    </ul>
</div>
</body></html>
"""

soup=BeautifulSoup(html,'html.parser')
h1=soup.select("div#main > h1")
# div태그에서 id가 main인 것의 하위의 h1
print('h1',h1)
# h1 [<h1>강의목록</h1>]
# print('h1',h1.string)
# 에러남. 왜냐하면 h1의 type이 list이기 때문에 바로 리스트의 속성에 접근 불가능.
print('h1',type(h1))
# h1 <class 'list'>
# 따라서 하나라도 반복문을 돌려야 함.
for z in h1:
    print(z.string)
# 강의목록
# 이렇게 하면 번거로우므로
h1=soup.select_one("div#main > h1")
print('h1',h1)
# h1 <h1>강의목록</h1>
print('h1',h1.string)
# h1 강의목록

list_li=soup.select("div#main > ul.lecs > li")
# 엄밀히 이야기하면 굳이 div#main으로 쓸 필요 X. 왜냐하면 유일한 것을 id로 잡기 때문에
for li in list_li:
    print("li >>> ",li.string)
# li >>>  Java 초고수 되기
# li >>>  파이썬 기초 프로그래밍
# li >>>  파이썬 머신러닝 프로그래밍
# li >>>  안드로이드 블루투스 프로그래밍
