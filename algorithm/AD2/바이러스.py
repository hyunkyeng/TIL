import sys
sys.stdin = open("바이러스.txt")

def DFS(n):
    global cnt
    if visited[n] == 0:
        visited[n] = 1
        cnt += 1
        for i in range(1, N+1):
            if data[n][i] == 1:
                DFS(i)

N = int(input())
M = int(input())
visited = [0]*(N+1)     #방문표시
data = [[0]*(N+1) for _ in range(N+1)]   #인접행렬
for i in range(M):
    s, e = map(int, input().split())
    data[s][e] = data[e][s] = 1   # 연결체크

cnt = 0
DFS(1)
print(cnt-1)