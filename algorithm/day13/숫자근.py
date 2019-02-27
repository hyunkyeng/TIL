def sum(str_N):
    total = 0
    for j in range(len(str_N)):
        total += int(str_N[j])
    return total

import sys
sys.stdin = open("숫자근.txt")

T = int(input())
max = 0
max_N = 0


for i in range(T):
    N = int(input())
    str_N = str(N)

    total = sum(str_N)
    while total >= 10:
        str_total = str(total)
        total = sum(str_total)


    if total > max:
        max = total
        max_N = N
    elif total == max:
        if max_N > N:
            max_N = N

print(max_N)