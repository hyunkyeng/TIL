import sys
sys.stdin = open("problem_GNS_input.txt", "r")
T = int(input())

for tc in range(T):
    temp = input()    # '#'이 있어서 받기 어렵다. 그냥 데이터의 len값을 받으면 되니까 안받아도 된다. 따라서 dumm로 받고 안쓴다.
    data = list(map(str, input().split()))
    count = [0]*10
    res = ""
    L = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in data:
        for j in range(len(L)):
            if i == L[j]:
                count[j] += 1
    for k in range(len(L)):
        res += count[k] * (L[k] + " ")

    print(f'#{tc+1} {res}')

