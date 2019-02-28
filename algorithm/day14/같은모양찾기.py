import sys
sys.stdin = open("같은모양찾기.txt")

M = int(input())
mArr = [list(map(str, input())) for _ in range(M)]
P = int(input())
pArr = [list(map(str, input())) for _ in range(P)]




imsipattern = []
cnt = 0
for i in range(0,M-P+1):
    for j in range(0,M-P+1):
        for l in range(P):
            imsipattern.append(mArr[i+l][j:j+P])
        if imsipattern == pArr:
            cnt += 1
        imsipattern = []

print(cnt)