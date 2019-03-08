import sys
sys.stdin = open("문제1.txt")

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    L = []
    for _ in range(N):
        L.append(list(map(int, input().split())))
    min = 100000

    for y in range(N-K+1):
        for x in range(N-K+1):
            right = 0
            left = 0
            for k in range(K):
                right += L[y+k][x+k]
                left += L[y+k][(x+K-1)-k]
            diff = right - left
            if diff < 0:
                diff = -1 * diff
            if min > diff:
                min = diff

    print("#{} {}".format(tc+1, min))
