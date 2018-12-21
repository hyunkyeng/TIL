# 내 풀이

# import random
# from bs4 import BeautifulSoup
# import requests

# numbers = random.sample(range(800, 838), 8)
# # print(numbers)
# for number in numbers:
#     print(f"\n {number}회차 당첨번호")
#     url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={number}"
#     req = requests.get(url).text
#     soup = BeautifulSoup(req, 'html.parser')
#     for lotto in soup.select('.ball_645'):
#         print(lotto.text, end = " ")
        


#선생님 풀이

import random
from bs4 import BeautifulSoup
import requests

numbers = random.sample(range(800, 838), 8)
for number in numbers:
    count = 0
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={number}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    lucky = soup.select(".ball_645")
    print(f"{number} 회차 당첨번호")
    for i in lucky:
        print(i.text, end = " ")
        count +=1
        if count == 6:
            print("+", end = " ")
    print()




# 100 회차 당첨번호
# 1 2 3 4 5 6 +7 
# 이렇게 8개가 출력. 