
# 최소거리

import sys, time
from time import strftime
sys.stdin = open("최적경로.txt")

start_time = time.time()
#순열
def perm(n, k):
    global length, sm_length
    if n == k:
        for i in range(2):
            if i == 0:
                j = 0
            else:
                j = -1
            len_x = se[i][0] - new_L[j][0]
            len_y = se[i][1] - new_L[j][1]
            if len_x < 0:
                len_x = -1 * len_x
            if len_y < 0:
                len_y = -1 * len_y
            length += len_x + len_y
        for i in range(N - 1):
            len_x = new_L[i][0] - new_L[i + 1][0]
            len_y = new_L[i][1] - new_L[i + 1][1]
            if len_x < 0:
                len_x = -1 * len_x
            if len_y < 0:
                len_y = -1 * len_y
            length += len_x + len_y
            if length > sm_length:
                length = 0
                return

        if length < sm_length:
            sm_length = length
        length = 0
    else:
        for i in range(k, n):
            new_L[i], new_L[k] = new_L[k], new_L[i]
            perm(n, k+1)
            new_L[i], new_L[k] = new_L[k], new_L[i]

T = 10
for tc in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    company = [L.pop(0), L.pop(0)]
    house = [L.pop(0), L.pop(0)]
    se = [company] + [house]
    sm_length = 10000000000000
    length = 0
    new_L = [[L[i], L[i+1]] for i in range(0, len(L), 2)]



    perm(N, 0)
    print('#{} {}'.format(tc+1, sm_length))
print(time.time() - start_time, 'seconds')



