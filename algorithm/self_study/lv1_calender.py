# Q. 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면 YYYY/MM/DD 형식으로 출력,
# 날짜가 유효하지 않을 경우, -1 을 출력

import sys
sys.stdin = open("lv1_calender.txt")

T = int(input())
for tc in range(1):
    N = input()
    print(N)

year = N[0:4]
month = N[4:6]
day = N[6:]
if month
# 딕셔너리로 풀까?
print(year, month, day)