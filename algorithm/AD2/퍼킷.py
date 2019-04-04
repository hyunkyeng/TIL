import sys
sys.stdin = open("퍼킷.txt")

def DFS(n, sin, ssun):
    global nmin
    if n >= N:
        if sin == 1 and ssun == 0:
            return
        gap = abs(sin - ssun)
        if gap < nmin:
            nmin = gap
        return
    DFS(n+1, sin, ssun)
    DFS(n+1, sin*data[n][0], ssun+data[n][1])


N = int(input())    # 재료 개수
data = [list(map(int, input().split())) for _ in range(N)]
# print(data)
nmin = float('inf')

DFS(0, 1, 0)
print(nmin)