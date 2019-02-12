import sys
sys.stdin = open("그래프경로.txt")

def dfs(t):
    global G, visited, L
    visited[t] = 1

    for w in range(V):
        if G[t][w] == 1 and visited[w] == 0:
            dfs(w)


T = int(input())
for tc in range(T):
    L = []
    V, E = map(int, input().split())
    V += 1
    for i in range(E):
        a, b = map(int, input().split())
        L.append(a)
        L.append(b)
    start, end = map(int, input().split())

    G = [[0 for _ in range(V)] for _ in range(V)]
    visited = [0 for _ in range(V)]

    for i in range(0, len(L), 2):
        G[L[i]][L[i + 1]] = 1


    dfs(start)


    print(f'#{tc+1} {visited[end]}')