import sys
sys.stdin = open("토너먼트카드게임.txt")

def rsp(group):
    dict = {}
    if len(group) == 1:
        dict[1] = group[0]
    if len(group) > 1:
        for j in range(0, len(group), 2):
            if group[j] + group[j+1] == 3:
                if group[j] == 2:
                    dict[j+1] = 2
                if group[j+1] == 2:
                    dict[j+2] = 2
            if group[j] + group[j+1] == 4:
                if group[j] == 1:
                    dict[j+1] = 1
                if group[j+1] == 1:
                    dict[j+2] = 1
            if group[j] + group[j+1] == 5:
                if group[j] == 3:
                    dict[j+1] = 3
                if group[j+1] == 3:
                    dict[j+2] = 3

    return dict


T = int(input())
for tc in range(1):
    N = int(input())
    L = list(map(int, input().split()))
    print(L)
    group1 = []
    group2 = []
    group3 = []
    group4 = []

    for i in range(1, N+1):
        if 1 <= i <= (1+N)//4:
            group1.append(L[i-1])
        if (1+N)//4 + 1 <= i <= (1+N)//2:
            group2.append(L[i-1])
        if (1+N)//2 + 1 <= i <= 3*((1+N)//4):
            group3.append(L[i-1])
        else:
            group4.append(L[i-1])
    print(group1)
    print(group2)

    print(rsp(group1))
    print(rsp(group2))
