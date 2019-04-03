import sys
sys.stdin = open("건물세우기.txt")

def dfs(n, nsum):
    global nmin
    if nsum > nmin:
        return
    if n >= N:
        if nsum < nmin:
            nmin = nsum
        return
    for i in range(N):
        if chk[i]:
            continue
        chk[i] = 1
        rec[i] = data[n][i]
        dfs(n+1, nsum + data[n][i])
        chk[i] = 0


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
nmin = 1000000
chk = [0] * N
rec = [0] * N

dfs(0, 0)
print(nmin)