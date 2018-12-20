# 파이썬 dicttionary 활용 기초

# dict = {
#     "대전": 23,
#     "서울": 30,
#     "구미": 20
# }

# print(type(dict.values()))

# Q. 평균을 구하세요.
# scores = {
#     "국어": 87,
#     "영어": 92,
#     "수학": 40
# }

# # value = score.values()
# # print(value)

# total_score = 0
# for score in scores.values():
#     # total_score = total_score + score 와 밑에 문장은 같은 문장이다. 
#     total_score += score

# average_score = total_score / len(scores)   
# print(total_score)
# print(average_score)

# 두번째 방법
# total_score = sum(score.values())
# average_score = total_score/len(scores)

# # Q.2 반 평균을 구하시오
# scores = {
#     "철수": {
#         "수학": 80,
#         "국어": 90,
#         "음악": 100
#     },
#     "영희": {
#         "수학": 70,
#         "국어": 60,
#         "음악": 50
#     }
# }

# # total_score = 0
# # print(scores.values())
# all_total = 0
# count = 0
# for score in scores.values():
#     totals = score.values()
#     # print(totals)
#     for total in totals:
#         all_total += total
#         count += 1


# average_score = all_total / count       
# print(all_total)
# print(average_score)

#     # total_score += score

# # print(scores["철수"])

# total_score = 0
# count = 0
# for person_score in scores.values():
#     for indivisual_score in person_score.values():
#         total_score += indivisual_score
#         count += 1

# print(total_score)
# average_score = total_score / count
# print(average_score)


# scores = {
#      "국어": 87,
#      "영어": 92,
#      "수학": 40
# }

# for key, value in scores.items():
#     print(key)

# Q.3 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

#선생님 풀이
# cities = {
#     "서울": [-6, -10, 5],
#     "대전": [-3, -5, 2],
#     "광주": [0, -2, 10],
#     "부산": [2, -2, 9]
# }

# # max(안에 리스트 넣기)
# # min(안에 리스트 넣기)

# hot = 0
# cold = 0
# hot_city = ""
# cold_city = ""
# count == 0

# for name, temp in cities.items():
#     if count == 0:
#         hot = max(city)
#         cold = min(temp)
#         hot_city = name
#         cold_city = name
#     else: 
#         # 최저 온도가 cold보다 추우면, cold 에 넣고
#         if min(temp) < cold:
#             cold = min(temp)
#             cold_city = name
#         #최고 온도가 hot보다 더 추우면, hot 에 널고
#         if max(temp) > hot:
#             hot = max(temp)
#             hot_city = name
#     count += 1

# print(f"{hot_city}, {cold_city}")


#내 풀이

# max_city = 0
# min_city = 0
# max_name = ""
# min_name = ""
# for name, temp in cities.items():
#     tempmax = max(temp)
#     if max_city < tempmax:
#         max_city = tempmax
#         max_name = name
#     tempmin = min(temp)
#     if min_city > min(temp):
#         min_city = min(temp)
#         min_name = name
# print(max_city)
# print(max_name)
# print(min_city)
# print(min_name)

# print(f"가장 더웠던 곳은 {max_name}, 가장 추웠던 곳은 {min_name}")


import requests
from bs4 import BeautifulSoup

url = "http://www.op.gg/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
rank = soup.select_one('.TierRank')