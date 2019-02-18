#Q. 각 자릿수의 합을 계산

import sys
sys.stdin = open("lv01_numbersum.txt")


N = input()
sum = 0
for i in N:
    sum += int(i)

print(sum)