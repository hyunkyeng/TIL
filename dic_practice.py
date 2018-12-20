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

# Q.2 반 평균을 구하시오
scores = {
    "철수": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "영희": {
        "수학": 70,
        "국어": 60,
        "음악": 50
    }
}

# total_score = 0
# print(scores.values())
all_total = 0
for score in scores.values():
    totals = score.values()
    # print(totals)
    for total in totals:
        all_total += total

scores_count = scores.count(0)
print(scores_count)
average_score = all_total        
print(all_total)
print(average_score)

    # total_score += score

# print(scores["철수"])
