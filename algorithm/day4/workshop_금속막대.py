import sys
sys.stdin = open("workshop_금속막대.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    res = []
    # print(L)

    C = [0] * 101
    for i in range(len(L)):
        C[L[i]] += 1
    # print(C)

    for i in range(int(len(L)/2)):
        if C[L[2*i]] == 1:
            res.append(L[2*i])
            res.append(L[2*i + 1])
    # print(res)
    while len(res) < len(L):
        for i in range(int(len(L)/2)):
            if res[-1] == L[2*i]:
                res.append(L[2 * i])
                res.append(L[2 * i + 1])
    res = " ".join(map(str, res))
    print(f'#{tc+1} {res}')






    # res = []
    # print(L)
    # for i in range(int(len(L)/2)):
    #     tup = (L[2*i], L[2*i+1])
    #     res.append(tup)
    # print(res)

