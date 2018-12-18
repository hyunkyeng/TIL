# import requests
# from bs4 import BeautifulSoup

# req = requests.get("https://finance.naver.com/sise/").text
# soup = BeautifulSoup(req, 'html.parser')
# kospi = soup.select_one("#KOSPI_now")
# print(kospi.text)

# import requests
# from bs4 import BeautifulSoup

# req = requests.get("https://land.naver.com/isale/").text
# soup = BeautifulSoup(req, 'html.parser')
# bu = soup.select_one("#selectedDvsn")
# print(bu.text)

# import requests
# from bs4 import BeautifulSoup

# req = requests.get("https://movie.naver.com/").text
# soup = BeautifulSoup(req, 'html.parser')
# movie = soup.select_one("#review1 > div > a")
# print(movie.text)

# import requests
# from bs4 import BeautifulSoup

# req = requests.get("https://www.naver.com/").text
# soup = BeautifulSoup(req, 'html.parser')
# search = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul")
# print(search.text)

# import requests
# from bs4 import BeautifulSoup

# req = requests.get("https://www.naver.com/").text
# soup = BeautifulSoup(req, 'html.parser')
# searchs = soup.select_one("#ah_1")
# for search in searchs:
#     rank = search.select("#ah_item")
#     print(rank.text)

import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'):
    rank = tag.select_one('.ah_r').text
    name = tag.select_one('.ah_k').text
    print(f'{rank}는 {name}입니다.')