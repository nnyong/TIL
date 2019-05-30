import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url="http://www.naver.com"

mem=req.urlopen(url)

# print(type(mem))
# print(type({}))
# print(type([]))
# print(type(()))

# print("geturl",mem.geturl())
# print("status",mem.status) #200, 404, 403, 500
# print("headers",mem.getheaders())
# print("info",mem.info) # headers의 줄바꿈버전
# print("code",mem.getcode()) # status와 같음.
# print("read",mem.read(20)) #가져올 만큼만 가져옴. 위에만 필요한 게 있으면 자를 수 있음.
# print("read",mem.read(50).decode('utf-8')) #문자열 깨지지 않게 하기 위해. 또는 euc-kr ...
print(urlparse("http://www.naver.com?test=test"))
