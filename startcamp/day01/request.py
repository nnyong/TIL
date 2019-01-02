import requests
import bs4

# response=requests.get("https://finance.naver.com/sise/").text
# soup=bs4.BeautifulSoup(response,'html.parser')
# result=soup.select_one('#KOSPI_now').text
# print(result)

response=requests.get("https://www.naver.com/").text
soup=bs4.BeautifulSoup(response,'html.parser')
result=soup.select_one('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul').text
print(result)

