def enQ(n):
    global last
    last += 1
    c = last
    p = c//2
    Q[last] = n
    while c > 1 and Q[p] > Q[c]:
        Q[p], Q[c] = Q[c], Q[p]
        c = p
        p = p//2
    return Q


import sys
sys.stdin = open("이진힙.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    Q = [0] * (N+1)
    last = 0
    sum = 0

    for i in L:
        enQ(i)
    while N // 2:
        sum += Q[N//2]
        N = N // 2
    print("#{} {}".format(tc+1, sum))

