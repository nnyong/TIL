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
      xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
      xmlns:dc="http://purl.org/dc/elements/1.1/"
      xmlns:taxo="http://purl.org/rss/1.0/modules/taxonomy/"
      xmlns:activity="http://activitystrea.ms/spec/1.0/" >
  <channel>
  <title>보도자료</title>
  <link>https://www.mois.go.kr</link>
  <description></description>
  <language>ko</language>
  <pubDate>WED, 29 MAY 2019 12:00:00 KST</pubDate>
      
      
          <item>
              <title><![CDATA[안전 소재 웹드라마 '안그래도 전부터' 아·태 지역서도 인정]]></title>
              <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=70972]]></link>
              <description><![CDATA[
                  안전 소재 웹드라마 '안그래도 전부터' 아·태 지역서도 인정<br />- 행안부 안전한TV 2019 아시아-태평양 스티비상 소셜미디어 혁신 분야 '은상' 수상 -<br /><br />행정안전부(장관 진영)가 운영하는 국내 유일의 재난안전 전문채널인 '안전한TV'에서 제작한 안전소재 웹드라마가 「2019 아시아-태평양 스티비상*’(2019 Asia-Pacific Stevie Awards)｣ 소셜미디어 혁신 분야 은상을 수상한다.<br />   * 아시아 권역 16개국의 개인이나 단체에서 이룬 혁신적인 업적(12개 부문)에 대해 시상, 올해 6회째로 시상식은 5.31.(금), 싱가포르 인터콘티넨털호텔에서 개최<br /><br />안전을 소재로 다룬 웹드라마 '안그래도 전부터'는 총 5편으로 제작된 시리즈물로 일상에서 겪을 수 있는 안전 문제를 자연스럽게 공감할 수 있도록 하고 있다.<br /><br />지난해('18년), 행정안전부 페이스북과 안전한TV 누리집, 유튜브 등 소셜미디어를 활용해 방영되었으며, 유튜브 조회수 37만 회를 기록하는 등 큰 호응을 받았다. <br />스티비상 주최측은 "다소 딱딱할 수 있는 안전 관련 정보를 젊은 층이 선호하는 웹드라마로 제작해 시청자의 반응을 높이 평가했다."라고 수상 배경을 밝혔다.<br /><br />아울러, 안전한TV*는 각종 재난‧안전사고 상황에서 일반 국민들이 실천할 수 있는 행동요령을 영상으로 제작‧보급 하고 있으며,<br />    * 누리집: www.safetv.go.kr / 유튜브: 안전한TV(구독자 수: 2만166명/ 5.23.기준)<br />올해부터는 매주 수요일 오전 11시 소셜미디어를 활용한 안전 생방송 <안전해주세요>를 통해 시청자들과 직접적인 소통 기회를 넓히고 있다. <br /><br />하병필 행정안전부 대변인은 "이번 수상을 계기로 국민의 눈높이에 맞는 생활 속 안전 영상물 제작을 확대하고, 누구나 쉽게 접근할 수 있도록 소셜미디어를 통해 확산해 나갈 계획이다."라고 말했다.<br /><br />* 담당 : 안전소통담당관실 김종선(044-205-1071)
                      ]]></description>
              <pubDate>WED, 29 MAY 2019 12:00:00 KST</pubDate>
              <author>안전소통담당관</author>
          </item>
      
          <item>
              <title><![CDATA[노후 유‧도선 현대화사업 본격 추진한다]]></title>
              <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=70971]]></link>
              <description><![CDATA[
                  노후 유‧도선 현대화사업 본격 추진한다<br />- 선령기준 초과 유‧도선 폐선에 따른 신규 건조 추진 -<br /><br />행정안전부(장관 진영)는 5월 30일 정부세종2청사에서 정부(행정안전부, 해양경찰청), 선박안전기술공단, 유‧도선안전협회, 금융기관(5개 기관), 조선조합(2개 기관) 등과 함께 노후 유‧도선 현대화사업 추진 활성화를 위한 업무협약을 체결한다.<br />협약식에는 행정안전부 재난안전관리본부장을 비롯하여 해양경찰청, 선박안전기술공단, 유‧도선안전협회, 산업은행, 기업은행, 부산은행, 수협은행, 신한은행, 한국조선공업협동조합, 한국조선해양기자재공업협동조합 등 11개 기관 책임자가 참석한다.<br /><br />세월호 사고 이후 노후 유‧도선에 대한 안전관리 강화를 위해 2016년 2월 3일부터 선령제도*가 신설(「유선 및 도선 사업법」 제4조의2 제1항 제1호)되었다.<br />   * (기본) 20년 ⇒ (연장) 25년(FRP‧목선은 25년 한정) ⇒ (연장) 30년(강선)<br />다만, 이미 면허를 받은 업체에서 보유하고 있는 유‧도선은 7년간 적용을 유예하여 유예기간이 종료되는 2023년 2월 3일을 시점으로 총 1,400여척 중 150여 척이 폐선 될 예정이다.<br />이에 따라, 선박 건조에 약 2년 정도가 소요되는 점을 감안하면 2020년부터는 본격적인 대체 건조가 필요하며, 향후 5년간 총 227척*을 대체 건조할 계획이다.<br />   * (대체 건조계획) ‘20년 65척, ’21년 37척, ‘22년 29척, ’23년 32척, ‘24년 64척<br /><br />이번 협약의 주요 내용을 살펴보면, 행정안전부와 해양경찰청은 “노후 유‧도선 현대화사업” 추진과 관련된 협력사업 지원(융자, 융자알선, 보조 등)에 대한 민·관 협력을 총괄하게 된다.<br />선박안전기술공단, 유‧도선안전협회, 금융기관, 조선조합 등 관계기관에서는 유‧도선 현대화사업과 관련된 △신규 건조 융자 △예산 절감 방안 △조선사 간 보증 △신규 건조 대상 업체에 대한 정보 및 자료 등 제공 △기타 상호 필요한 사항을 협력하게 된다.<br /><br />이를 통해 중고 선박 도입을 억제하고 신규 건조를 유도함으로써 유‧도선의 안전과 조선 산업분야 일자리 창출을 통한 지역경제 활성화가 기대된다.<br />특히, 조선조합에 따르면 소형 조선업계의 경우 매년 10% 이상의 인력 및 매출액 증가*, 퇴직자 재취업 효과, 관련 조선기자재 등 후방산업도 활성화 될 것으로 보고 있다.<br />   * 한국조선공업협동조합 회원사 소형조선소(83개사) ‘15~’17년 평균 매출액 5,300억여 원 대비 ‘20년 이후 5년 평균 유‧도선 신조물량 매년 500억여 원 증가 예상<br /><br />김계조 행정안전부 재난안전관리본부장은 “많은 사람이 이용하는 유‧도선의 지속적인 안전기반을 확보하고, 중소 조선선사의 경영 안정과 일자리 창출에 따른 지역경제 활성화를 위해 관계기관이 적극 동참해 주길 바란다.”라고 말했다.<br /><br />* 담당 : 안전제도과 우주형(044-205-4149)
                      ]]></description>
              <pubDate>WED, 29 MAY 2019 12:00:00 KST</pubDate>
              <author>안전제도과</author>
          </item>
      
          <item>
              <title><![CDATA[지방세관계법 운영예규, 국민의 지방세 길라잡이로 거듭나다]]></title>
              <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=70970]]></link>
              <description><![CDATA[
                  지방세관계법 운영예규, 국민의 지방세 길라잡이로 거듭나다<br />-행안부「지방세관계법 운영예규」제정, 국가법령정보센터에 공개-<br /><br />그 동안 행정 내부적으로 운영되던 지방세 관련 지침이 ｢지방세관계법 운영예규｣ 형태로 국민들이 알기 쉽게 공개된다.<br />행정안전부(장관 진영)는 지방세관계법*의 통일적 운영과 납세자 예측가능성 향상을 위해, ｢지방세관계법 운영예규｣를 제정하여 6월 1일부터 시행한다고 밝혔다.<br />    * 4개 법률(지방세기본법, 지방세징수법, 지방세법, 지방세특례제한법)<br /><br />지방세 부과·징수의 세부 운영기준으로 활용될 ‘운영예규’는 지방세관계 4개 법률을 각 장으로 하여 총 4개의 장(章)과 539개 조문으로 구성되어 있다.<br />특히 지방세징수법이 종전 지방세기본법에서 분리되어 제정(2017.3.) 됨에 따라 관련 예규를 새롭게 정비하고, 최근(2017년∼2019년) 지방세관계법 개정사항*과 법원판례, 심판결정, 법령해석 등을 반영하여 42개 조문을 추가하였다.<br />   * 지방세징수법 제정(2017.3.27.), 2017년∼2019년 지방세관계법령 개정 내용<br /><br />이번 제정안의 특징은 종전의 ‘지방세관계법률 기본통칙’이란 명칭을 국민들이 이해하기 쉽도록「지방세관계법 운영예규」로 바꾸었으며,<br />지방세 납세자 권리보호와 국민의 알 권리 제고를 위해 대외적으로 고시되는 ‘예규’(행정규칙의 일종)로 상향하여 최초로 법제처 국가법령정보센터에 공개*된다.<br />  * ｢훈령·예규 등의 관리에 관한 규정(6조)｣ 훈령 및 예규의 발령일로부터 10일 이내에 법제처장이 정하는 정부입법 관련 전산시스템에 등재하여야 한다.<br /><br />나아가 행정안전부(법령자료집), 지방세정보화시스템(위택스), 지방세연구원(법령정보시스템) 누리집에도 게시하여 국민들이 최대한 쉽게 접할 수 있도록 하였다.<br /><br />고규창 행정안전부 지방재정경제실장은 “이번 지방세 예규집 제정으로 과세관청의 합리적인 세정운영을 제고하고, 납세자의 지방세 이해에 길라잡이 역할을 할 것으로 기대한다.”라고 말했다.<br /><br />* 담당 : 지방세정책과 오정의(044-205-3808)
                      ]]></description>
              <pubDate>WED, 29 MAY 2019 12:00:00 KST</pubDate>
              <author>지방세정책과</author>
          </item>
      
          <item>
              <title><![CDATA[민원실 방문 외국인주민 위한 통역서비스 확대한다]]></title>
              <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=70969]]></link>
              <description><![CDATA[
                  민원실 방문 외국인주민 위한 통역서비스 확대한다<br />- 행안부, 외국인주민 대상 민원편의 제공서비스 확산 추진 -<br /><br />행정안전부(장관 진영)는 외국인주민이 민원실을 방문할 때, 민원신청 절차 등을 자국어로 정확하게 안내받을 수 있도록 외국인주민을 위한 통역서비스를 확산해 나갈 계획이다.<br />‘17년말 기준 외국인주민은 1,861천명(전체인구대비 3.6%)으로, 최근 3년간 평균 5.6%* 증가하고 있고, 관련 민원수요도 급증하고 있어 외국인주민에 대한 민원편의서비스 제공의 확대가 필요한 시점이다.<br />    * (15년) 1,711천명 → (16년) 1,765천명 → (17년) 1,861천명<br />이를 위해, 행정안전부는 지방자치단체에서 시행되고 있는 외국인주민 대상 민원서비스 운영 실태를 조사*하였다.(’18.12.)<br /><br />외국인주민 대상 민원서비스 운영실태 조사결과에 따르면, <br />-(민원처리실태) 외국인주민의 주요민원은 가족관계등록 관련 5종,* 체류지 변경, 각종 제증명 발급(출입국사실증명서 등), 여권 발급 등이며<br />    * 혼인, 출생, 이혼, 개명, 창설신고<br />-(민원종류) 지자체별*, 국적별 분포 및 입국목적에 따라 차이를 보임<br />    * (농어촌 지역) 국제결혼 등에 따른 가족관계등록 관련민원이 주종, (중소기업체 밀집지역) 외국인근로자 관련 체류지 변경 등 제증명 관련민원 수요 다수 <br />-(민원편의 제공서비스) 외국인주민에 대한 민원업무 통역(동행‧전화)서비스를 전국 243개 지자체 중 49개 기관(20%)에서 제공하고 있으며 민원서식 번역본을 제공(54개 기관)하고, 일부지자체에서는 생활쓰레기 배출‧지방세 납부방법 등 생활정보안내(번역본) 서비스를 제공 중이다.<br /><br />행정안전부는 외국인주민이 체감할 수 있는 민원편의서비스의 조기 확산을 위해, 우선 지자체에서 제공 중인 통역서비스 등 우수사례를 전파하고, 지자체별 실정에 적합한 서비스의 제공을 권고할 예정이다.<br />이번에 전파하는 민원편의서비스는 민원인 통역서비스 우수사례(3종), 민원서식 번역서비스, 생활법률‧지방세 납부안내 번역서비스 등이다.<br />또한, 하반기까지 「외국인주민 민원‧생활정보안내 표준안」을 마련하여 민원실을 방문하는 외국인주민들에게 꼭 필요한 민원편의서비스 및 생활정보 제공을 확산해 나갈 계획이다. <br /><br />윤종인 행정안전부 차관은 “외국인주민의 민원업무 처리를 지원하기 위한 통역서비스를 확대하고, 일상생활에서 겪는 불편함이 최소화되도록 해 나가겠다.”라며 “앞으로도 외국인주민을 포함한 사회적약자에 대한 민원서비스를 면밀히 살펴, 서비스 이용 시 불편함이 없도록 지속적으로 노력할 것이다.”라고 밝혔다.<br /><br />* 담당 : 민원제도혁신과 신윤성(044-205-2444)
                      ]]></description>
              <pubDate>WED, 29 MAY 2019 12:00:00 KST</pubDate>
              <author>민원제도혁신과</author>
          </item>
      
          <item>
              <title><![CDATA[온라인 민원, 한 번의 신청으로 원하는 만큼 출력 가능해진다]]></title>
              <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=70968]]></link>
              <description><![CDATA[
                  온라인 민원, 한 번의 신청으로 원하는 만큼 출력 가능해진다<br />- ｢출력 매수 제한조치 삭제｣ 등 민원처리법 시행령 개정 -<br /><br />그간 온라인으로 민원서류를 발급하는 경우 설치해야 했던 플러그인을 간소화할 수 있도록 하는 등 민원 제도가 정비된다.<br />행정안전부(장관 진영)는 ｢민원 처리에 관한 법률 시행령 일부개정령안｣이 29일 국무회의를 통과했다고 밝혔다.<br />이번 개정안의 주요 내용은 다음과 같다.<br /><br />첫째, 온라인에서 민원서류 발급 시 플러그인 등 별도 프로그램 설치가 동반되었던 ‘출력매수 제한 조치’를 삭제했다.<br />그 동안은 민원을 ‘정부24’ 등 온라인으로 신청하고 직접 민원서류를 출력하는 경우, ‘출력 매수 제한조치’를 적용해야만 정식 ‘공문서’로 인정되었다.<br />이로 인해 수수료가 없는 민원이나 누구나 신청할 수 있는 공시성 민원 등에도 일괄적으로 ‘출력 매수 제한조치’가 적용되어 플러그인 설치 등 불편이 초래되었다.<br />이번 개정안은 민원인이 온라인으로 출력한 민원서류를 공문서로 보는 요건 중 ‘출력 매수의 제한조치’를 삭제하도록 하여, 공시성 민원이나 수수료가 없는 민원은 해당 플러그인 설치 없이도 출력할 수 있도록 했다.<br /><br />둘째, 민원처리 절차에 ｢부패방지법｣상 시민고충처리위원회의 고충민원 처리절차를 포함시켰다.<br />고충민원을 해당 행정기관뿐만 아니라 ｢부패방지법｣에 따른 국민권익위원회와 시민고충처리위원회에도 신청할 수 있음을 안내하여, 민원인의 권익을 두텁게 보호한다.<br /><br />셋째, 민원을 우수하게 처리한 공무원, 부서에 대해 포상 등을 할 수 있는 근거를 마련했다.<br />민원을 우수하게 처리한 공무원이나 부서에 대해 행정기관의 장이 포상 등 인센티브를 부여할 수 있는 근거를 마련하여, 민원공무원의 사기를 진작하고 보다 친절한 민원서비스를 시행할 수 있도록 했다.<br /><br />진영 행정안전부 장관은 “출력매수 제한조치를 삭제하는 이번 민원처리법 시행령 개정안 통과로 민원인은 별도의 플러그인을 설치하는 번거로움이 사라지게 되고, 행정기관은 수수료 부과 등의 필요에 따라 자율적으로 제도를 운영할 수 있게 되었다.”라며, “앞으로도 국민생활과 관련된 불편과 부담을 개선해 나가도록 노력하겠다.”라고 밝혔다.<br /><br />* 담당 : 민원제도혁신과 박진혜(044-204-2448)
                      ]]></description>
              <pubDate>WED, 29 MAY 2019 10:00:00 KST</pubDate>
              <author>민원제도혁신과</author>
          </item>
      
          <item>
              <title><![CDATA[“나는 조국해방의 첫 번째 선구자”, 그는 역시 영웅이었다.]]></title>
              <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=70942]]></link>
              <description><![CDATA[
                  “나는 조국해방의 첫 번째 선구자”, 그는 역시 영웅이었다.<br /> - 안중근 의사 의거 관련 러시아 극동지역 신문기사 수집·공개-<br /><br />“죽음이 두렵지 않다. 고문도 두렵지 않다. 나의 이성과 심장은 너희들에 의해 병들었다. 죽으면서 나는 기쁘다. 나는 조국 해방의 첫 번째 선구자가 될 것이다.” <br />일제의 첫 심문부터 사형집행까지 안중근 의사의 당당하고 의연한 모습과 발언 내용 등을 소개한 러시아 언론 보도가 확인되었다.  <br /><br />행정안전부 국가기록원은 28일 설립 50주년 및 공공기록물법 제정 20주년을 맞아 러시아 블라디보스톡, 하바로프스키 등의  지역신문이 보도한 안중근 의사 관련 기사 24건을 수집·공개한다. <br />공개된 기록물은 국가기록원이 지난 2015년 독립운동과 우리 동포 관련 기록물이 다수 있을 것으로 추정되는 러시아 극동지역을 대상으로 기획·수집하던 중 발굴된 것인데, 안 의사 의거일 다음 날인 1909년 10월 27일부터 1910년 4월 21일까지 안의사 관련 보도이다. <br />그동안 안중근 의사 관련 러시아 신문기사가 단편적으로 소개된 적은 있으나, 러시아 극동지역 여러 신문의 관련 기사를 망라하여 공개한 것은 이번이 처음이다.<br /><br />특히 이들 신문에는 시종일관 의연했던 안중근 의사의 모습,  차이쟈고우에서의 의거 준비, 체포과정, 하얼빈 의거에 대한 러시아인들의 인식 등이 구체적으로 담겨 있어 사료적 가치가 매우 높다.<br /><br /> - 달리니 보스톡지(紙)」는 의거일 이틀 뒤인 1909년 10월 28일자에 26일 아침 9시 최전선 열병식에 참석하기 위하여 하얼빈역에 도착한 이토 공작(당시 조선 통감)은 치명적 총상을 입었고, 조선인으로 밝혀진 범인이 체포되었다고 보도했다.(붙임 1 번역문 참조) <br /><br /> - 「쁘리 아무리예지(紙)」 11월 2일자는 10월 24일 정오, 하얼빈에서 남쪽으로 가는 차이쟈고우의 우편열차 정거장에서 안중근, 우덕순, 조도선이 내리는 것부터 다음날 아침, 거사를 위해 안중근이 하얼빈으로 떠날 때 서로 눈물을 흘리며 큰 절로 인사하는 장면까지 르포형식으로 게재했다. 아울러 일본 총영사관에서 있었던 첫 심문에서 “죽음을 두려워하지 않는다. 당신들의 고문도 두렵지 않다. 나의 이성과 심장은 조국에서 일본인들에 의해 병을 얻었다. 죽으면서 나는 기쁘다. 나는 조국 해방을 위해 첫 번째 선구자가 될 것이다.”라고 말한 안 의사의 진술을 실었다.(붙임2 번역문 참조)<br /><br /> - 「보스토치나야 자랴지(紙)」 11월 4일자는 “이토 사살은 우리 조국 역사의 마지막 장이 아니며, 아직 살아 있는 것이 기쁘며, 나의 유골에 자유가 비출 것이다.”라고 말한 안 의사의 진술을 그대로 실었다.(붙임3 번역문 참조)<br /><br />신문들은 안중근 의사가 현장을 지휘하는 러시아 장교에 의해 기차역으로 옮겨진 뒤 감옥으로 이송되는 과정도 상세히 보도했다. <br /><br /> - 「쁘리 아무리예지(紙)」11월 6일자는 1일 있었던 이송상황을 구체적으로 전하고 있다. 기차에 오르는 안중근, 우덕순, 조도선의 발에 족쇄가 채워져 있었고, 안중근은 손에 수갑까지 채워져 있었다. 열차에는 마지막으로 안중근이 올라탔다. 그의 얼굴은 창백하였으며, 주변 사람들에게 완전히 무관한 모습을 보였다고 묘사했다.(붙임4 번역문 참조)<br /><br />또한 신문은 안중근 의사의 법정진술과 사형선고 당시의 상황도 상세하게 소개하고 있다. <br /> <br /> - 「쁘리 아무리예지(紙)」 1910년 2월 27일자는 사형을 선고한 2월 26일 재판 상황에 대해 보도하였는데, 1시간 동안 자신의 행위에 대한 정당성을 주장하였고, 모든 사람들이 그에게 마음이 끌리는 것 같았으며, 안중근의 어머니는 가치 있는 죽음을 맞이하라는 마지막 인사말을 전한 것으로 보도하였다.(붙임5 번역문 참조)<br /><br />특히, 안중근 의사의 매장지와 관련된 보도기사가 주목을 끈다. 「우수리스까야 아끄라이나지(紙)」 1910년 4월 21일자는 안중근 의사는 사형 직후 교도소의 예배당으로 옮겨졌다가, 지역의 기독교 묘지에 매장된 것으로 보도하였다.(붙임 6 번역문 참조) 종전 안중근 의사의 매장지는 교도소 내의 묘지로 알려져 있었다.<br /><br />이번 공개와 관련 이소연 국가기록원장은 “안중근 의사와 하얼빈 의거에 대한 러시아의 인식뿐만 아니라, 의거 준비, 체포와 일본영사관 인계과정 등 사후 조치 과정이 상세하게 묘사되어 있어 사료적 가치가 높은 것으로 안다.”라며, “안중근 의사 의거 110주년을 맞아 독립정신을 실천했던 안 의사의 의연하고 당당한 모습을 국민과 함께 하고자 공개하게 되었다.”라고 밝혔다.<br /><br />* 담당 : 행정지원과 최중기(042-481-6232)
                      ]]></description>
              <pubDate>TUE, 28 MAY 2019 15:00:00 KST</pubDate>
              <author>행정지원과</author>
          </item>
      
          <item>
              <title><![CDATA[강원 원주, 전남 순천에 「사회적경제 유통지원센터」 생긴다.]]></title>
              <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=70941]]></link>
              <description><![CDATA[
                  강원 원주, 전남 순천에 「사회적경제 유통지원센터」 생긴다.<br />- 사회적경제기업에 새로운 판로 제공, 공동 홍보마케팅 등 기대 -<br /><br />판로 확보를 위해 고민하던 사회적경제기업에 희소식이 생겼다. 행정안전부(장관 진영)는 강원(원주), 전남(순천)에 「사회적경제 유통지원센터」를 조성하기로 했다.<br />작년에 시범사업으로 선정된 인천과 충남을 포함하여 4개 권역에 사회적경제의 유통거점이 만들어지는 것이다.<br /><br />「사회적경제 유통지원센터」는 지역사회에 흩어져서 활동하던 마을기업(행정안전부), 협동조합(기획재정부), 사회적기업(고용노동부), 자활기업(보건복지부) 등이 공동으로 유통하고 판매하는 시설로, 문재인 정부에서 핵심과제로 추진하고 있는 사회적경제 활성화의 일환이다.<br />앞으로 유통지원센터는 사회적경제기업에 새로운 판로를 제공하고, 공동 홍보·마케팅, 기업 간 교류·협력을 통해 자생력을 높여 주는 역할을 수행하게 된다.<br /><br />먼저, 원주 혁신도시에 위치하게 될 강원 유통지원센터는 지리적 여건으로 어려움을 겪고 있는 물류 환경을 개선하기 위해 통합물류의 중심지로 조성한다.<br />완공이 되면 도내 사회적경제기업들이 중심이 되어 운영 중인 ‘강원 곳간’ 직매장(2개소), 샵인샵(11개소), 온라인 쇼핑몰(2개소) 등에서 유통되는 제품들이 지금보다 빠르게 소비자에게 전달될 수 있을 것으로 기대된다.<br />특히, 혁신도시 안에 자리 잡은 공공기관과의 협업을 통해 공공구매를 활성화하고, 기업간 협력·상생의 장으로도 조성할 계획이다.<br /><br />순천시 도시재생지역 내 빈집을 리모델링하는 전남 유통지원센터는 전남 동부지역 사회적경제기업들에 유통 거점이 될 전망이다.<br />1층에는 사회적경제기업들의 제품을 판매하고, 2층에는 기업들의 역량 교육과 상호 교류하는 공유공간으로 조성하며, 3층에는 라운지 형식의 열린카페를 조성하여 관광객을 비롯해 누구나 편안하게 휴식을 취하며 사회적경제를 체험하도록 꾸민다.<br />또한, 기획상품과 공동브랜드를 개발하고 온라인 판매를 확대하기 위한 유통망 확보 등 판로 다각화를 모색할 예정이다.<br /><br />한편, 작년 하반기에 선정되었던 인천과 충남도 사업추진에 박차를 가하고 있다.<br />인천지역 120개 사회적경제기업이 참여하는 인천 유통지원센터는 마을카페를 비롯해 지역 대학생, 아파트 주민들이 사회적경제를 체험하고 제품을 구매할 수 있도록 조성하며, 9월부터 운영한다.<br />충남 유통지원센터는 충남 100여개 사회적경제기업들이 설립한 “따숨상사 협동조합”이 주축이 되어 10월 개점을 목표로 분주히 움직이고 있다.<br />특히, 국토부 도시재생사업으로 추진하는『문화 플랫폼 단지』내에 ‘판매장’을 조성하여 방문객 유입과 사회적경제 제품 홍보 등 시너지 효과를 기대하고 있다.<br /><br />김현기 행정안전부 지방자치분권실장은 “사회적경제 유통지원센터를 통해 기업들은 보다 많은 제품을 판매할 수 있고, 국민들은 사회적경제와 그 가치를 배우고 체험할 수 있는 상생의 장이 될 것이다.”라며 “사회적경제 유통지원센터가 사회적 가치를 실현하는 거점 공간으로 자리 잡을 수 있도록 적극 지원하겠다.”라고 말했다.<br /><br />* 담당 : 지역공동체과 정태욱(044-205-3435)
                      ]]></description>
              <pubDate>TUE, 28 MAY 2019 12:00:00 KST</pubDate>
              <author>지역공동체과</author>
          </item>
      
          <item>
              <title><![CDATA[차세대 예술가들의 부활전,「2019 실패박람회 in 전주」]]></title>
              <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=70940]]></link>
              <description><![CDATA[
                  차세대 예술가들의 부활전,「2019 실패박람회 in 전주」<br /> - 5.31, 전주에서 춘천과 대전에 이어 실패박람회 세 번째 개최 -<br /><br />2019 실패박람회의 세 번째 여정이 “실패는 두 번째 기회입니다”를 주제로 전주 한옥마을 일원에서 5.31(금)~6.2(일)에 시작된다.  <br />올해 실패박람회는 강원도(5.15~17)에서 시작하여 대전(5.21~23)으로 이어지면서 연일 성황리에 개최되고 있다.  <br /><br />이번 전주 박람회에서는 천년고도 예향의 도시라는 문화적 특성에 맞춰 전통문화예술을 계승하는 차세대들이 대거 등장할 예정이다.<br />차세대 예술가들은 실패로 인한 좌절에서 그치는 것이 아니라, 실패를 통해 영감을 발견하고, 패자부활을 위한 다양한 시도와 ‘망한 작품’의 겨룸을 통해서 실패 경험을 당당하게 드러낼 것이다.<br />구조적으로 비정규직일 수밖에 없는 예술가들이 펼치는 ‘부활전’으로서의 실패박람회는 재미있는 이야기(詮) 또는 아름다운 전시(展示)이고, 자기와의 치열한 겨룸(戰)이며, 나의 과거이자 동시에 전진(前進)이다. <br /><br />주목되는 프로그램은 ‘실패 사례 공모전’ 당선작을 미디어아트와 판소리로 연출한 ‘개막식’, 300인의 차세대 예술가가 들려주는 ‘실패밴드’와 실패를 주제로 한 ‘릴레이 공연’, 의미 있는 실패 사례를 뽑는 ‘국민숙의’, 실패 사연을 응원하는 ‘실패 라디오’ 등이다. <br />한편 재도전 지원을 위하여 17개의 민간협력기관이 참여하는 ‘정책마당’은 상담부스를 통해 소상공인 재기지원, 재취업?일자리 지원, 신용회복, 심리 등에 대하여 전문가 상담을 제공할 예정이다. <br /><br />김승수 전주시장은 “한해 천만 명이 찾는 글로벌 문화관광 도시 전주에서 다양한 사람들이 함께 실패를 공감하는 축제가 되기를 바란다.”라며, “실패가 삶의 새로운 가치로 자리잡을 수 있도록 새로운 패러다임의 축제로 거듭나도록 노력할 것”이라고 덧붙였다. <br />아울러 이번 행사를 준비해 온 이성원 전주 사회적경제지원단 단장은 “유네스코 음식창의도시 전주에서 개최하는 실패박람회를 통해 많은 분들이 전주의 맛과 멋과 흥을 만끽할 수 있도록 하겠다.”고 강조했다. <br /><br />전년도에 서울에서 처음 개최한 실패박람회를 올해에 지방으로 확산 추진 중인 김현기 행정안전부의 지방자치분권실장은 “앞서 강원도 춘천과 대전에서 권역별 실패박람회가 지역민들의 많은 관심과 사랑 속에 치러진 만큼 전주에서도 문화예술의 실패사례를 주제로 한 특별한 행사가 되어 주기를 기대하며, 박람회의 취지대로 실패 경험을 말하고 공감하며 더불어 해결책을 찾아 재도전을 응원하는 따뜻한 공동체 구현의 장이 되기를 바란다.”고 밝혔다.<br /><br />* 담당 : 주민참여협업과 윤태웅(044-205-3443)
                      ]]></description>
              <pubDate>TUE, 28 MAY 2019 12:00:00 KST</pubDate>
              <author>주민참여협업과</author>
          </item>
      
          <item>
              <title><![CDATA[포용과 참여 위한 정부혁신, 전 세계에 알린다]]></title>
              <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=70939]]></link>
              <description><![CDATA[
                  포용과 참여 위한 정부혁신, 전 세계에 알린다<br />- 행정안전부, 제6차 OGP 글로벌서밋에서 열린 정부 활동 공유 -<br /><br />우리나라의 포용과 참여를 위한 정부혁신 노력을 세계 79개국에 알리는 계기가 마련된다.<br />행정안전부(장관 진영)는 5월 29일부터 31일(현지시각)까지 2박 3일 일정으로 캐나다 오타와에서 개최되는 ‘제6차 OGP 글로벌서밋’에 정부혁신조직실장을 수석대표로 한 대표단을 파견한다.<br /><br />‘제6차 열린정부파트너십(Open Government Partnership, 이하 OGP) 글로벌서밋’은 열린 정부를 지향하는 국제협의체인 OGP와 의장국 캐나다가 주최하는 고위급 회의로서 ‘포용, 참여, 성과’를 주제로 열린다.<br /> 이번 회의는 주최국의 정상인 캐나다 저스틴 트뤼도(Justin Trudeau) 총리가 주재하고, OGP 회원인 79개국 장관급 인사와 20개 지방자치단체장, 시민사회단체 관계자들이 참석한다.<br /><br />OGP 운영위원국으로 활동하는 행정안전부는 29일 OGP 운영위 장관회의를 시작으로, 30일 디지털 시대의 신뢰 회복 제하 장관급 세션에서 정부의 주요 국정과제인 정부혁신에 대한 그 간의 추진 성과를 세계 각국과 공유한다. <br />아울러, 포용, 참여, 성과를 주제로 우리나라의 추진 계획을 발표한다. 먼저, ‘포용’ 분야에서는 사회적 가치 중심의 정부 운영을 소개하며 공공서비스로 사각지대를 해소하는 사례를 알릴 예정이다. <br />‘참여’와 관련해서는 국정운영의 핵심적인 과정에 국민 참여를 확대하는 정책 및 제도 등이 공유된다.<br /> 예산(국민참여예산제), 법령(국민참여법령심사제) 등 분야에 국민 참여 노력과 함께 정책 기획단계에서 이행, 평가에 이르기까지 전 과정에 국민 참여를 확대해 나가기 위한 노력이 소개된다.<br />아울러, 온오프라인 국민 참여 기제인 ‘광화문1번가 열린소통포럼’의 운영성과와 추진방향 등도 참석자들의 이목을 끌 것으로 기대된다.<br />마지막으로, 디지털 시대의 도전과제를 해결하기 위한 ‘성과’와 관련 개인정보 보호, 빅데이터 활용 행정 등 첨단 디지털 기술을 활용한 대한민국 정부의 행정혁신 사례들을 중점적으로 강조한다.<br /><br />또한, 도로시 베어(Dorothee Bar) 독일 디지털부 장관, 밤방 브로드조네고로(Bambang Brodjonegoro)인도네시아 국가개발기획부 장관, 산자이 프라드한(Sanjay Pradhan) OGP 사무총장과 양자회담을 통해 열린 정부 확산을 위한 협력 분야에 대해 논의한다.<br /><br />행정안전부는 이번 회의를 통해 우리의 정부혁신을 세계에 알리고 확산하는 한편 열린 정부를 위한 국제적인 노력에 더욱 적극적으로 동참한다는 계획이다.<br />이재영 행정안전부 정부혁신조직실장은 “이번 회의는 전 세계 열린 정부 리더들이 한 자리에 모여 열린 정부를 만들기 위한 노력을 공동으로 모색하는 자리”라며, “대한민국이 추진하고 있는 정부혁신의 목표와 OGP의 목표인 투명성 증진, 부패척결, 시민참여 활성화가 궤를 같이 하는 만큼, 우리나라가 국제적인 혁신 노력의 모범사례가 될 수 있기를 희망한다.”라고 말했다.<br /><br />* 담당 : 혁신기획과 이유진(044-205-2218)
                      ]]></description>
              <pubDate>TUE, 28 MAY 2019 12:00:00 KST</pubDate>
              <author>혁신기획과</author>
          </item>
      
          <item>
              <title><![CDATA[행안부「정보지식인 퀴즈 대회」개최(5.28~5.31)]]></title>
              <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=70882]]></link>
              <description><![CDATA[
                  행안부「정보지식인 퀴즈 대회」개최(5.28~5.31)<br />- 행정안전부 전 직원 대상 정보화 역량 강화 추진 -<br /><br />행정안전부(장관 진영)는 5월 28일부터 31일까지 4일간 행정안전부  소속 전 직원이 참여하는「정보지식인 퀴즈 대회」를 개최한다.<br /><br />이번 대회는 4차 산업혁명 및 지능 정보화시대에 대비하여 개인정보보호 및 정보보안 인식을 고양하고, 반드시 알아야 할 업무용 정보시스템 활용방법, 정보화 관련 규정 등 정보화 역량을 강화하기 위하여 추진하게 되었다.<br /> <br />행정안전부는 지난 3월부터 5월까지 본부 및 소속· 산하기관 전 직원을 대상으로 개인정보보호 등 정보화 역량에 대한 순회교육을 실시하였다. 본 교육은 총 28회에 걸쳐 2,700여명이 참석하였으며, 이번 퀴즈대회는 본「정보화 역량 교육」의 교육 내용을 중심으로 진행한다.<br />퀴즈 내용은 지난 교육에서 특히 중점을 둔 개인정보 보호, 정보 보안, 공공데이터 관리, 통계관리, 업무관리시스템(하모니) 이용 등 총 5가지 핵심분야에서 10개 문항을 출제하였다. 행정안전부 직원이면 업무관리시스템 배너를 통해 누구나 손쉽게 퀴즈대회에 참여할 수 있으며, 우수 직원에게는 소정의 상품(문화상품권 등)을 전달하여 직원 참여도를 제고할 계획이다.<br /><br />이인재 행정안전부 기획조정실장은 “4차 산업혁명에 따라 변화하는 정보화 환경에 맞는 행정서비스 제공하기 위해 최선을 다할 것”이라며, “이번 대회를 통해 행정안전부 소속 직원들의 정보보안 인식 및 정보화 역량이 더욱 향상되기를 기대한다.”고 말했다.<br /><br />* 담당 : 정보통계담당관 한재식(044-205-1646)
                      ]]></description>
              <pubDate>MON, 27 MAY 2019 12:00:00 KST</pubDate>
              <author>정보통계담당관</author>
          </item>
      
          <item>
              <title><![CDATA[소상공인 부담 완화 위해 지방공공기관 결제수단 확대]]></title>
              <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=70881]]></link>
              <description><![CDATA[
                  소상공인 부담 완화 위해 지방공공기관 결제수단 확대<br />- 지방공공기관의 예산편성·집행기준 개정으로 제로페이, 직불카드 사용가능 -<br /><br />행정안전부(장관 진영)는 소상공인의 수수료 부담완화를 위하여 지방공공기관이 모바일 간편결제시스템(이하 ‘제로페이’)을 사용할 수 있도록 5월 28일「지방공기업 예산편성기준」과「지방출자출연기관 예산집행기준」을 개정한다.  <br /><br />이번 개정 주요골자는 지방공공기관(지방공기업, 지방출자출연기관)이 업무추진비 사용 시 “제로페이*”와 “직불카드”를 사용할 수 있도록 결제 수단 확대 근거를 마련하는 것이다.<br />    * 휴대폰 등에 앱을 설치하여 공동 QR코드 방식으로 결제를 하면, 즉시 대금 입금이 소비자 계좌에서 가맹점 계좌로 이체하는 방식<br />현재 지방공공기관은 신용카드(클린카드)로만 결제가 가능한데, 이번 개정을 통해 제로페이와 직불카드를 사용함으로써, 카드 수수료를 신용카드 보다 낮추거나 없애 소상공인의 부담이 완화*될 것으로 기대된다.<br />    * 연매출 8억원이하 수수료율 : 신용카드(0.8∼1.4%), 직불카드 (0.5∼1.1%), 제로페이(0%)<br /><br />제로페이와 직불카드를 사용하려는 개별 지방공공기관은 올해 상반기 중 중소기업벤처부가 구축하는 제로페이 법인용 시스템에 자체 예산회계시스템을 연계해야 한다. <br />이와 더불어 제로페이와 직불카드를 사용한 때에는 사용 즉시 대금이 지급되는 만큼, 회계책임성을 강화하기 위해 회계관계관으로 하여금 증명서류 등을 명확히 확인하도록 하는 자체 회계규정 정비도 필요하다. <br /> <br />고규창 행정안전부 지방재정경제실장은 “이번 제도개선으로 전국 151개 지방공사?공단과 702개 지방출자출연기관이 제로페이와 직불카드를 사용할 수 있는 근거가 마련되는 만큼, 소상공인들의 카드 수수료 부담완화에 크게 기여할 것으로 기대한다.”라고 밝혔다. <br /><br />* 담당 : 공기업지원과 최영묵(044-205-3988)
                      ]]></description>
              <pubDate>MON, 27 MAY 2019 12:00:00 KST</pubDate>
              <author>공기업지원과</author>
          </item>
      
          <item>
              <title><![CDATA[새로운 을지태극연습, 국민과 정부와 군이 함께 한다.]]></title>
              <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=70880]]></link>
              <description><![CDATA[
                  새로운 을지태극연습, 국민과 정부와 군이 함께 한다.<br />- 2019 을지태극연습 5월 27일부터 올해 처음 실시 - <br /><br />행정안전부(장관 진영)는 5월 27일부터 30일까지 4일 동안 시·군·구 이상 행정기관과 공공기관·단체 및 중점관리대상업체 등 4천여개 기관에서 48만여 명이 참여하는 을지태극연습을 실시한다고 밝혔다.<br />을지태극연습은 국가위기상황에 대응하고 전시에 대비하는 민·관·군 합동 정부연습으로 안보환경의 변화와 한미 연합 군사연습 중단 방침에 따라 을지연습을 잠정 유예하면서 대안으로 새로운 정부연습 모델로 개발하여 실시하게 되었다.<br /><br />이번에 실시하는 을지태극연습이 예년의 연습과 다른 점은 다음과 같다.<br /><br />먼저, 대형 재난·테러 등 비군사적 요인도 국가 안보 위협으로 고려하는 포괄안보 개념을 적용한 ‘국가위기 대응연습’을 실시함으로써 대규모 복합재난에 대한 국가재난관리 역량을 강화한다.<br />이어서, 전시대비 연습은 한국군 단독연습인 태극연습과 연계하여 향후 전시작전통제권 환수에 대비하고 주변 안보환경에 영향을 받지 않는 독자적이고 안정적인 연습체계를 마련한다.<br />실제훈련에서는 영상회의 시스템, 재난안전통신망, 위성방송(SNG)차량, KT 스카이십(skyship) 등 제4차 산업혁명 기술을 적용한 최첨단 장비를 활용하여 지휘통제기구와 훈련 현장 간 신속한 정보 공유와 의사소통이 가능하도록 하였다.<br />뿐만 아니라 연습시기를 8월에서 5월로 변경하여 태풍 등 자연재난에 영향을 받지 않고 하계휴가 및 국회 일정과 겹치지 않는 시기에 실시함으로써 연습에 더욱 집중할 수 있도록 하였다.<br /><br />을지태극연습의 주요 내용은 다음과 같다.<br /><br />제1부 국가위기 대응연습(27일~28일 16:00)과 제2부 전시대비연습(28일 16:00~30일)으로 구분하여 시행한다.     <br />국가위기 대응연습에서는 전국적으로 복합재난이 발생하는 상황을 가정해 위기대응조직(중대본, 중수본, 지대본 등) 가동 훈련과 상황판단회의를 실시하고 안보분야 위기관리매뉴얼 과제 토의를 진행한다.<br />또한, 국방부 재난지원부대 등이 대거 참여하는 민·관·군 합동 실제훈련을 실시하고 40여 개 기관이 동시에 영상으로 참여하는 국무총리 주재 ‘국가위기관리 상황평가회의’를 진행하여 대규모 복합재난에 대한 종합적 대처 상황을 점검한다.<br />특히, 재난현장의 대처상황을 재난안전통신망, 위성방송(SNG)차량, KT 스카이십(skyship), 드론 등 최첨단 영상 전송 장비를 활용하여 중앙재난안전상황실(세종)로 실시간 전송함으로써 신속하고 정확한 정보 공유와 의사소통이 가능하여 통합적 재난관리체계를 구축할 수 있다. <br />전시대비연습은 불시 공무원 비상소집훈련, 통합방위사태 선포절차훈련, 전시직제편성훈련 등을 실시하고 사이버 안보 역량을 강화하기 위해 사이버 테러, 위성항법장치(GPS) 교란 등 사이버 위협에 대한 대응 훈련도 실시한다.<br />아울러, 국민과 함께하는 연습이 되도록 다양한 비상상황에 대한 주민대피 행동요령 실습과 방독면 착용방법, 심폐소생술 교육 등 국민생활과 밀접한 안전교육을 체험방식으로 진행한다.<br /><br />진영 행정안전부 장관은 “국민과 정부와 군이 함께하는 을지태극연습을 통해 국가위기대응 역량을 총체적으로 점검하고, 각종 위기관리 계획과 매뉴얼을 보완하는 기회가 될 것으로 기대한다.”라고 말했다.<br /><br />* 담당 : 비상대비훈련과 이광희(044-205-4352)
                      ]]></description>
              <pubDate>SUN, 26 MAY 2019 12:00:00 KST</pubDate>
              <author>비상대비훈련과</author>
          </item>
      
          <item>
              <title><![CDATA[12개국 고위급 공무원, 한국 전자정부 수출기업 만난다]]></title>
              <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=70879]]></link>
              <description><![CDATA[
                  12개국 고위급 공무원, 한국 전자정부 수출기업 만난다<br />- 행안부, 상반기 전자정부 정책관리자 과정 운영 -<br /><br />행정안전부(장관 진영)는 상반기 전자정부 정책관리자 과정(5.27.~31.)을 진행하여 개도국 전자정부 발전과 우리기업들의 수출을 지원한다.  <br />‘전자정부 정책관리자 과정’은 한국형 전자정부 모델의 글로벌 확산과 전자정부 수출기업의 해외 진출을 지원하기 위해 행정안전부가 상·하반기로 진행하는 전자정부 역량 강화 과정이다.<br />이번 상반기 전자정부 정책관리자 과정에는 12개국에서 전자정부를 담당하는 고위급 공무원 12명이 참여하였다.<br /><br />참가자들은 ‘한국의 전자정부 정책 및 비전’ 소개를 시작으로 12개국의 전자정부 정책 및 추진현황을 서로 공유하고 한국의 전문가 조언과 함께 각국의 상황을 분석하는 프로그램에 참여한다.<br />삼성 SDS, 국가정보자원관리원, 국가기록원, K-ICT 빅데이터센터, 판교 테크노밸리 등 현장 방문을 통해 참가자들이 궁금해 하는 전자정부 구축의 노하우를 직접 체험한다. <br />또한 해외사업을 추진하는 전자정부 기업들과 연수생들 간의 간담회를 추진하여 전자정부 구축 협력을 모색할 수 있는 기회를 마련하였다.<br /><br />○ 참여국 중 튀니지, 파라과이, 세르비아는 한국과 전자정부분야 협력이 활발한 나라들이다. 이번 초청을 계기로 전자정부 협력센터 및전자정부 공동사업에 대한 더욱 구체적인 사업목표를 설정하는 등 사전협력이 강화될 것으로 보인다. <br />○ 우즈베키스탄의 경우 한국의 오픈데이터, 빅데이터 정책에 특별한 관심과 함께 지난 4월 정상회담이후 전자정부 협력을 더욱 강화하고 있다.  <br />○ 우간다는 ‘16년 6월 상호양해각서(MOU) 체결을 이후로 꾸준히 협력하여 ’18년에는 정부행정 효율화를 위한 시스템이 수출되었고, 사물인터넷(IoT), 클라우드, 데이터 분야의 협력에 관심을 표명하였다.<br />○ 동아프리카의 마다가스카르는 구축된 전자정부 서비스가 많지 않았으나 클라우드 활성화, 오픈데이터, 빅데이터 정책에 관심이 높았고, 온두라스는 구축된 전자정부 서비스가 있음에도 전자정부 성과관리나 서비스분야 실행에 있어서 다양한 분야의 경험 공유를 요청하였다.      <br />○ 에콰도르는 ‘16-’17년에 선거개표 전송 시스템이 수출된바 있는데, 클라우드 활성화 정책 및 스마트시티, 인공지능(AI)분야 등 신기술을 활용한 디지털 정부 혁신이 주요 관심사이다.  <br />○ 태국은 중소기업 혁신지원 시스템 구축 정책 자문사업이 추진된 바 있고, 이번 연수에서는 전자정부 서비스 분야에서 우리나라가 실행하고 있는 전자정부 성과평가 관리 등 많은 정책 관련 경험을 희망하였다.  <br />○ 말레이시아는 버스정보, 교통센터, 스마트시티 구축 등 한국시스템이 다수 진출하였는데, 한국의 사물인터넷(IoT) 정책과 전자정부법 및 제도에 높은 관심을 보였다.<br /> <br />최장혁 행정안전부 전자정부국장은 “이번 상반기 전자정부 정책관리자 과정을 통해 한국의 전자정부 도입을 검토하는 국가의 고위공무원들에게 한국의 선도적인 전자정부 정책, 사이버보안시스템, 혁신적인 클라우드 정책 등을 경험할 수 있는 기회를 제공하겠다.”라며 “특히 참가자들과 전자정부 구축 기업들 간 간담회를 추진하여 한국 전자정부의 해외 진출을 적극 지원하겠다.”라고 밝혔다. <br /><br />* 담당 : 글로벌전자정부과 김나미(044-205-2788)
                      ]]></description>
              <pubDate>SUN, 26 MAY 2019 12:00:00 KST</pubDate>
              <author>글로벌전자정부과</author>
          </item>
      
  </channel>
  </rss>
  ```

  

* 구글에서 my ip api 검색

  <https://www.ipify.org/>