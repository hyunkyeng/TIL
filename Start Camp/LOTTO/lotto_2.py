import random
import requests
import json
from pprint import pprint

# 0. random 으로 로또번호를 생성합니다. 
# 1. api를 통해 우승 번호를 가져옵니다. 
# 2. 0번과 1번을 비교하여 나의 등수를 알려준다. 

# Hint
# 1. url 요청 보내서 정보를 가져옵니다. 
#     - jsom 으로 받는다. (딕셔너리로 접근 가능)
# 2. api 의 당첨번호와 보너스 번호를 저장하고
# 3. 뽑은게 몇등인지 하는거 뽑으세요. 

# url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
# res = requests.get(url)
# lotto = res.json()
# api_1 = lotto["drwtNo1"]
# api_2 = lotto["drwtNo2"]
# api_3 = lotto["drwtNo3"]
# api_4 = lotto["drwtNo4"]
# api_5 = lotto["drwtNo5"]
# api_6 = lotto["drwtNo6"]
# api_b = lotto["firstPrzwnerCo"]

# api = [api_1, api_2, api_3, api_4, api_5, api_6, api_b]
# # print(api)
# api_set = set(api)
# # print(api_set)
# bonus = [api_b]
# bonus_set = set(bonus)
# # print(api_b)
# count = 0
# while True: 
#     lotto = random.sample(range(1,46), 6)
#     lotto_set = set(lotto)
#     if len(api_set & lotto_set) == 3:
#         print(f"5등입니다.(당첨번호 3개 일치) {count}번만에 당첨이 되었습니다.")
#     elif len(api_set & lotto_set) == 4:
#         print(f"4등입니다.(당첨번호 4개 일치) {count}번만에 당첨이 되었습니다.")
#     elif len(api_set & lotto_set) == 5:
#         print(f"3등입니다.(당첨번호 5개 일치) {count}번만에 당첨이 되었습니다.")
#     elif len(api_set & lotto_set) == 5 and len(api_set & bonus_set) == 1:
#         print(f"2등입니다.(당첨번호 5개+보너스 일치) {count}번만에 당첨이 되었습니다.")
#     elif len(api_set & lotto_set) == 6:
#         print(f"1등입니다.(당첨번호 6개 일치) {count}번만에 당첨이 되었습니다.")
#         break

#     count += 1


# 선생님 풀이

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()

winner = []
for i in range(1, 7):
    winner.append(lotto[f"drwtNo{i}"])

bonus = lotto["bnusNo"]
print("이번주 당첨번호: " + str(winner))
print("보너스 번호: " + str(bonus))

count = 0
while True:
    count += 1
    my_numbers = sorted(random.sample(range(1, 46), 6))
    matched = len(set(winner) & set(my_numbers))

    if matched == 6:
        print("1등")
    elif matched == 5:
        if bonus in my_numbers:
            print("2등")
        else:
            print("3등")
    elif matched == 4:
        print("4등")
    elif matched == 3:
        print("5등")
        print(count, "번만에 당첨되셨습니다.")
        money = format(count*1000, ',')
        print("사용한 돈은", money)
        break
    else:
        print("꽝")