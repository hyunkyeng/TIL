import requests  #pip install requests
from bs4 import BeautifulSoup   #bash 창에 pip install bs4

url = 'http://www.op.gg/summoner/userName='
username = 'Hide on bush'
response = requests.get(url+username).text
soup = BeautifulSoup(response, 'html.parser')
wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
print(wins.text)
print(loses.text)