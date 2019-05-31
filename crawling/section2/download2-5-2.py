from bs4 import BeautifulSoup
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# """ """는 줄바꿈이 포함되어 있는 문자열
html="""
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>
"""

# print('html',html)
soup=BeautifulSoup(html, 'html.parser')
#soup에 이 내용이 객체로 만들어져서 할당 됨.
print('soup',type(soup))
# soup <class 'bs4.BeautifulSoup'>
print('prettify',soup.prettify())
# 자동으로 html 들여쓰기해서 출력함.
h1=soup.html.body.h1
print('h1',h1)
# h1 <h1>파이썬 BeautifulSoup 공부</h1>
print('h1',type(h1))
# h1 <class 'bs4.element.Tag'>
print(h1.string)
# 파이썬 BeautifulSoup 공부
#위처럼 가져오면 h1 문자열만 출력

# p의 경우 html>body에 두개 있음.
p1=soup.html.body.p
print(p1)
# <p>태그 선택자</p> 첫번째 노드를 가져옴.
p2=p1.next_sibling
print('p2',p2)
# p2 #각 줄 뒤에 \n이 숨겨져 있기 때문에 next_sibling에 접근하면 \n으로 감.
p2=p1.next_sibling.next_sibling
print('p2',p2)
# p2 <p>CSS 선택자</p>
p3=p1.previous_sibling.previous_sibling
print('p3',p3)
# p3 <h1>파이썬 BeautifulSoup 공부</h1>

# 위처럼 직접 접근으로 태그를 순차적으로 접근할 수 있음.

print("h1 >> ",h1.string)
print("p >> ",p1.string)
print("p >> ",p2.string)
# h1 >>  파이썬 BeautifulSoup 공부
# p >>  태그 선택자
# p >>  CSS 선택자

# but, 주로 위처럼 쓰진 않음.
# 이유 웹페이지 지속적으로 크롤링하는데 있던 태그가 사라지거나 html에 변경이 생길 경우
