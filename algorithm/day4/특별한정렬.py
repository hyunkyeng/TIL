import sys
sys.stdin = open("특별한정렬_input.txt")

T = int(input())

for tc in range(T):
    N = input()
    L = list(map(int, input().split()))
    r = []
    for i in range(len(L)-1):
        midx = i
        if i % 2 == 0:
            for j in range(i+1, len(L)):
                if L[midx] < L[j]:
                    midx = j
            L[i], L[midx] = L[midx], L[i]
        else:
            for j in range(i+1, len(L)):
                if L[midx] > L[j]:
                    midx = j
            L[i], L[midx] = L[midx], L[i]

    print(f'#{tc+1}', end=" ")
    for i in range(10):
        print(L[i], end=' ')
    print()
