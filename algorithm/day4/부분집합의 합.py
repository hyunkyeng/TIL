import sys
sys.stdin = open("부분집합의합_input.txt")

T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


for tc in range(T):
    N, K = map(int, (input().split()))
    L = []
    count = 0
    for i in range(1 << len(A)):
        s = []
        for j in range(len(A)):
            if i & (1 << j):
                s.append(A[j])
        L.append(s)
    for k in range(len(L)):
        if len(L[k]) == N and sum(L[k]) == K:
            count += 1
    print(f'#{tc+1} {count}')