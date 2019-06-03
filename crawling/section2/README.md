### 190530

## 크롬 개발자 도구

* ##### DOM 구조 분석(요소검사)

* ##### 선택자 추출 

  원하는 요소 copy -> **copy selector**

   ex) #gnbServiceList > ul > li:nth-child(3) > a

  gnbServiceList가 id인 애의 ul 태그의 li태그의 3번째 자식의 a 태그(?)

* ##### Console 도구

  자바스크립트 console에서 바로 실행 가능

* ##### Source-로딩 한 리소스 분석 및 디버깅

  source탭은 일단 패쓰,

* ##### 네트워크 탭 및 기타

  network탭에서 F5 누르면,

  이미지 파일, 동영상 파일, html파일 등 볼 수 있음.

  

  ##### Preserve log 체크박스 선택 시, 타이밍이나 불러오는 데 걸린 시간들이 새로고침 시에 누적됨!

  capture screenshots 선택 후 새로고침하면, 페이지가 로드되는 각 시간동안 어떤 요소들이 로드되고, 그 시간은 어떤지 나눠서 보여줌. (사이트가 로드되는 과정 순차적으로 볼 수 있음.)

  

  memory탭에서는 현재 성능에 대한 메모리 누수가 없는지, 병목현상이 없는지, 어떤 부분에서 로드가 오래 걸리는지 확인 가능

  

  performance 레코드 버튼 누르고 stop하면 현재 한 행동에 대해서 로딩되는 타이밍, 순서를 알려줌. network 탭의 capture screenshots이랑 똑같은 것!

  

  application 탭 현재 구조 볼 수 있고, 쿠키 값이 저장되어 있음.



## 파이썬 urllib을 활용해 웹에서 필요한 데이터 추출하기

###### 하고자 하는 것

* html 다운받아 필요한 텍스트, 정보 파싱 -> DB or TXT, 엑셀, JSON파일로 만들어서 다른 server로 전송



##### https://docs.python.org

: 버전 선택 후, Library Reference에서 다양한 메소드 사용법 알 수 있음.

* urlretrieve

  저장 -> open('r') -> 변수에 할당 -> 파싱 -> 저장. 

  파싱이 필요없는 데이터 한 번에 다운로드 받는 경우 좋음.

  ```python
  imgUrl="https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2F20100113_10%2Fdbwjd177_12633924830421M1mY_jpg%2Fc6f7b8de2_yousongyee_dbwjd177.jpg&type=b360"
  htmlURL="http://google.com"
  
  savePath1="c:/test1.jpg"
  savePath2="c:/index.html"
  
  dw.urlretrieve(imgUrl,savePath1)
  dw.urlretrieve(htmlURL,savePath2)
  ```

  

* urlopen

  urlopen: 변수 할당 -> 파싱 -> 저장(db,...)

  중간 작업이 필요한 경우는 urlopen이 좋음.

  ```python
  imgUrl="https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2F20100113_10%2Fdbwjd177_12633924830421M1mY_jpg%2Fc6f7b8de2_yousongyee_dbwjd177.jpg&type=b360"
  htmlURL="http://google.com"
  
  savePath1="c:/test1.jpg"
  savePath2="c:/index.html"
  
  f=dw.urlopen(imgUrl).read() #이미지 데이터를 f에 할당
  f2=dw.urlopen(htmlURL).read()
  ```



* open, write, close

  ```python
  saveFile1=open(savePath1,'wb') # w:write, r:read, a: add, b:binary
  saveFile1.write(f) # f데이터를 쓰겠다.
  saveFile1.close()
  ```



* with

   close는 with로 대체할 수 있다.

  ```python
  with open(savePath2,'wb') as saveFile2:
      saveFile2.write(f2)
  ```



* urlopen

  ```python
  import sys
  import io
  import urllib.request as req
  from urllib.parse import urlparse
  
  sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
  sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
  
  url="http://www.naver.com"
  
  mem=req.urlopen(url)
  
  # 자료형 알아보기
  print(type(mem))
  <class 'http.client.HTTPResponse'>
  
  print(type({}))
  <class 'dict'>
  
  print(type([]))
  <class 'list'>
  
  print(type(()))
  <class 'tuple'>
  
  print("geturl",mem.geturl())
  geturl https://www.naver.com/
      
  print("status",mem.status) #200, 404, 403, 500
  status 200
  
  print("headers",mem.getheaders())
  headers [('Server', 'NWS'), ('Date', 'Thu, 30 May 2019 08:36:51 GMT'), ('Content-Type', 'text/html; charset=UTF-8'), ('Transfer-Encoding', 'chunked'), ('Connection', 'close'), ('Set-Cookie', 'PM_CK_loc=74bdbf0085a509af54734802db7f160506cc2ac92a0629476334060f7caca72e; Expires=Fri, 31 May 2019 08:36:51 GMT; Path=/; HttpOnly'), ('Cache-Control', 'no-cache, no-store, must-revalidate'), ('Pragma', 'no-cache'), ('P3P', 'CP="CAO DSP CURa ADMa TAIa PSAa OUR LAW STP PHY ONL UNI PUR FIN COM NAV INT DEM STA PRE"'), ('X-Frame-Options', 'DENY'), ('X-XSS-Protection', '1; mode=block'), ('Strict-Transport-Security', 'max-age=63072000; includeSubdomains'), ('Referrer-Policy', 'unsafe-url')]
  
  print("info",mem.info) # headers의 줄바꿈버전
  info <bound method HTTPResponse.info of <http.client.HTTPResponse object at 0x0000018E12CEDF98>>
  
  print("code",mem.getcode()) # status와 같음.
  code 200
  
  print("read",mem.read(20)) #가져올 만큼만 가져옴. 위에만 필요한 게 있으면 자를 수 있음.
  read b'<!doctype html>\n\n\n\n\n'
  
  print("read",mem.read(50).decode
  <html lang="ko">
  <
        
  print(urlparse("http://www.naver.com?test=test"))
  ParseResult(scheme='http', netloc='www.naver.com', path='', params='', query='test=test', fragment='')
  ```

  

* urlencode

  ```python
  API="https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
  
  values={
      'ctxCd':'1012'
  }
  print('before',values)
  before {'ctxCd': '1012'}
  
  params=urlencode(values)
  print('after',params)
  after ctxCd=1012
  
  url=API+"?"+params
  print("요청 url",url)
  요청 url https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1012
  
  reqData=req.urlopen(url).read().decode('utf-8')
  print('출력',reqData)
  출력 <?xml version="1.0" encoding="UTF-8" ?>
  <rss version="2.0"
  ...
  ```

  

* 구글에서 my ip api 검색

  <https://www.ipify.org/>



### 190531

# BeautifulSoup 사용법 및 간단 웹 파싱 기초

* 웹 파싱: 궁극적으로 어떤 html파일(태그, 요소, 속성 등으로 구성) 잘 분석해서 내가 원하는 데이터의 위치를 찾는 것.

  ex) 이미지 경로, 동영상 경로, 문자, 숫자 등

* BeautifulSoup이용하면 손쉽게 파싱 가능. 
  * anaconda prompt에서 beautifulSoup 설치

    ```cmd
    pip install beautifulsoup4
    conda list #설치완료 확인
    ```



*  urljoin

  ```python
  from urllib.parse import urljoin
  
  baseUrl="http://test.com/html/a.html"
  print(">>",urljoin(baseUrl,"b.html"))
  # >> http://test.com/html/b.html 치환되어서 나옴.
  print(">>",urljoin(baseUrl,"sub/b.html"))
  # >> http://test.com/html/sub/b.html
  print(">>",urljoin(baseUrl,"../index.html"))
  # >> http://test.com/index.html 상위로 가서 치환되어서 나옴.
  print(">>",urljoin(baseUrl,"../img/img.jpg"))
  # >> http://test.com/img/img.jpg
  print(">>",urljoin(baseUrl,"../css/img.css"))
  # >> http://test.com/css/img.css
  ```

  

* """ """

  줄 바꿈이 포함되어 있는 문자열

  ```python
  html="""
  <html>
  <body>
  <h1>파이썬 BeautifulSoup 공부</h1>
  <p>태그 선택자</p>
  <p>CSS 선택자</p>
  </body>
  </html>
  """
  ```

  

* beautifulsoup 기초

  ```python
  soup=BeautifulSoup(html, 'html.parser')
  #soup에 이 내용이 객체로 만들어져서 할당 됨.
  print('soup',type(soup))
  print('prettify',soup.prettify())
  h1=soup.html.body.h1
  print('h1',h1)
  # h1 <h1>파이썬 BeautifulSoup 공부</h1>
  print('h1',type(h1))
  # h1 <class 'bs4.element.Tag'>
  print(h1.string)
  
  p1=soup.html.body.p
  print(p1)
  p2=p1.next_sibling
  print('p2',p2)
  p2=p1.next_sibling.next_sibling
  print('p2',p2)
  p3=p1.previous_sibling.previous_sibling
  print('p3',p3)
  ```

  * prettify() : html 자동 들여쓰기해서 출력.

  * soup.html.body.h1: soup 객체 html태그 안의 body 태그 안의 h1태그 선택

  * h1.string: 문자열만 출력

  * p 태그는 여러 개 있으므로 soup.html.body.p의 경우 첫번째 노드만 가져옴.

    따라서, next_sibling을 이용해 다음 p태그에 접근.

    `""" """`의 경우, 각 줄 마지막에 \n이 포함되어 있기 때문에 next_sibling을 하면 \n가 선택됨.

    따라서, next_sibling.next_sibling을 해주어야 다음 태그가 출력됨. 물론 한 줄 쓰기 경우엔 그럴 필요 없음.

  * previous_sibling의 경우도 next_sibling과 마찬가지이나 이전 태그로 이동.



* 태그 선택자 이용해 한번에 가져오기

  ```python
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
  a=soup.find_all("a",string="daum")
  print('a',a)
  b=soup.find("a")
  print('b',b)
  c=soup.find_all("a",limit=3)
  print('c',c)
  d=soup.find_all(string=["naver","google"])
  print('d',d)
  print('d',type(d))
  # d <class 'bs4.element.ResultSet'>
  
  for a in links:
      print('a',type(a),a)
      href=a.attrs['href']
      # attrs: 속성. 
      txt=a.string
      print('txt >> ',txt,'href >> ',href)
  ```

  * .find_all("a"): 모든 a태그 가져옴.
  * .find_all("a",string="daum"): a 태그 중 string이 조건에 맞는 것만 가져옴.

  * .find("a"): a태그 상위 1개만 가져옴.

  * .find_all("a",limit=3): "a" 태그 중 상위 3개만 가져옴.

  * .find_all(string=["naver","google"]): string에 해당하는 string만 가져옴. 보통 쓸일 x.

  * type이 resultset의 경우 for문 이용해서 출력해야함.

  * .attrs[key 값]: key 속성의 value 출력

    href=""에서 href가 key ""가 value



* css 선택자 이용해서 조건에 맞는 element 가져오기

  ```python
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
  print('h1',h1)
  print('h1',type(h1))
  for z in h1:
      print(z.string)
  h1=soup.select_one("div#main > h1")
  print('h1',h1)
  print('h1',h1.string
  
  list_li=soup.select("div#main > ul.lecs > li")
  for li in list_li:
      print("li >>> ",li.string)
  ```

  * .select("div#main > h1"): div태그에서 id가 main인 것의 하위의 h1

  * print('h1',h1.string)
    에러남. 왜냐하면 h1의 type이 list이기 때문에 바로 리스트의 속성에 접근 불가능.

     따라서 하나라도 반복문을 돌려야 함.

  * 하지만 번거로움 피하기 위해 .select_one 사용하면 됨. 하나인 경우!



### 190603

# BeautifulSoup 사용법 및 간단 웹 파싱 기초(2)



* 정규표현식

  참고사이트: <http://pythonstudy.xyz/python/article/401-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D-Regex>

  | 패턴       | 설명                                                         | 예제                                                  |
  | ---------- | ------------------------------------------------------------ | ----------------------------------------------------- |
  | ^          | 이 패턴으로 시작해야 함                                      | ^abc : abc로 시작해야 함 (abcd, abc12 등)             |
  | $          | 이 패턴으로 종료되어야 함                                    | xyz$ : xyz로 종료되어야 함 (123xyz, strxyz 등)        |
  | [문자들]   | 문자들 중에 하나이어야 함. 가능한 문자들의 집합을 정의함.    | [Pp]ython : "Python" 혹은 "python"                    |
  | [^문자들]  | [문자들]의 반대로 피해야할 문자들의 집합을 정의함.           | [^aeiou] : 소문자 모음이 아닌 문자들                  |
  | \|         | 두 패턴 중 하나이어야 함 (OR 기능)                           | a \| b : a 또는 b 이어야 함                           |
  | ?          | 앞 패턴이 없거나 하나이어야 함 (Optional 패턴을 정의할 때 사용) | \d? : 숫자가 하나 있거나 없어야 함                    |
  | +          | 앞 패턴이 하나 이상이어야 함                                 | \d+ : 숫자가 하나 이상이어야 함                       |
  | *          | 앞 패턴이 0개 이상이어야 함                                  | \d* : 숫자가 없거나 하나 이상이어야 함                |
  | 패턴{n}    | 앞 패턴이 n번 반복해서 나타나는 경우                         | \d{3} : 숫자가 3개 있어야 함                          |
  | 패턴{n, m} | 앞 패턴이 최소 n번, 최대 m 번 반복해서 나타나는 경우 (n 또는 m 은 생략 가능) | \d{3,5} : 숫자가 3개, 4개 혹은 5개 있어야 함          |
  | \d         | 숫자 0 ~ 9                                                   | \d\d\d : 0 ~ 9 범위의 숫자가 3개를 의미 (123, 000 등) |
  | \w         | 문자를 의미                                                  | \w\w\w : 문자가 3개를 의미 (xyz, ABC 등)              |
  | \s         | 화이트 스페이스를 의미하는데, [\t\n\r\f] 와 동일             | \s\s : 화이트 스페이스 문자 2개 의미 (\r\n, \t\t 등)  |
  | .          | 뉴라인(\n) 을 제외한 모든 문자를 의미                        | .{3} : 문자 3개 (F15, 0x0 등)                         |

  예제1

  ```python
  import re
  text ="에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
  regex =re.compile("에러\s\d+")
  mc =regex.findall(text)
  print(mc)
  # 출력: ['에러 1122', '에러 1033']
  ```

  예제2

  ```python
  import re
   
  text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
   
  regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
  matchobj = regex.search(text)
  areaCode = matchobj.group(1)
  num = matchobj.group(2)
  fullNum = matchobj.group()
  print(areaCode, num) # 032 232-3245
  ```

  예제3

  ```python
  import re
   
  text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
   
  regex = re.compile(r'(?P<area>\d{3})-(?P<num>\d{3}-\d{4})')
  matchobj = regex.search(text)
  areaCode = matchobj.group("area")
  num = matchobj.group("num")
  print(areaCode, num)  # 032 232-3245
  </num>
  ```



* 정규 표현식 활용

  ```python
  li=soup.find_all(href=re.compile(r"^https://"))
  ```

  ^https:// -> https://로 시작

  r: rawdata

  ```python
  li=soup.find_all(href=re.compile(r"da"))
  ```

  da -> da를 포함



* 다양한 css 선택자 이용해서 가져오기

  ```python
  print("1", soup.select("li:nth-of-type(4)")[1].string)
  #각 li 태그 그룹의 4번째 요소 선택
  print("2",soup.select_one("#ac-list > li:nth-of-type(4)").string)
  print("3",soup.select("#ac-list > li[data-lo='cn']")[0].string)
  print("4",soup.select("#ac-list > li.alcohol.high")[0].string)
  # 클래스 2개인 경우 .으로 연결
  
  param={"data-lo":"cn","class":"alcohol"}
  print("5",soup.find("li",param).string)
  # 딕셔너리형태도 들어갈 수 있다.
  print("6",soup.find(id="ac-list").find("li",param).string)
  # 이렇게 하면 정확하게 접근을 한 것이지만 5번째 방법이 더 가독성, 효율성이 좋음.
  
  for ac in soup.find_all("li"):
      if ac['data-lo']=='us':
          print('data-lo==us',ac.string)
  ```

  가져오는 방법만 다를 뿐이지, 궁극적으로 가져 올 값은 같음.

  방법은 스스로 하는 것에 따라 다름.



* function 이용하기

  ```python
  def car_func(selector):
      print("car_func",soup.select_one(selector).string)
      
  car_func("#gr")
  # car_func Grandeur
  car_func("li#gr")
  car_func("ul > li#gr")
  car_func("#cars #gr")
  car_func("#cars > #gr")
  # 공백으로 연결은 자손
  # > 로 연결은 자식
  car_func("li[id='gr']")
  ```

  

* lambda 이용하기

  ```python
  car_lambda=lambda q: print("car_lambda",soup.select_one(q).string)
  
  car_lambda("#gr")
  car_lambda("li#gr")
  car_lambda("ul > li#gr")
  car_lambda("#cars #gr")
  car_lambda("#cars > #gr")
  car_lambda("li[id='gr']")
  ```

  

# BeautifulSoup을 활용한 웹 파싱 실습

* 변하는 데이터들을 자동화 시켜두어, 일정한 시간에 가져와 데이터베이스에 저장하기.

* 다음 금융 시가총액 상위 종목 가져오기

  다음 금융 사이트

  

* 네이버 금융 Top 10 종목 가져오기

  

* 인프런 추천 강좌 10개 가져오기

  

  ###### 실습: 다음 실시간 인기 검색어 + link 스크랩핑 해보기