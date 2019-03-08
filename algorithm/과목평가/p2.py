import sys
sys.stdin = open("문제2.txt")


def dfs(y, x):
    global L, visited, max, flag

    visited[y][x] = 1
    if max < L[y][x]:
        max = L[y][x]
    L[y][x] = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if L[ny][nx] != 0 and visited[ny][nx] == 0:
                dfs(ny, nx)


T = int(input())
for tc in range(T):
    N = int(input())
    L = []
    for _ in range(N):
        L.append(list(map(int, input().split())))
    visited = [[0 for _ in range(N)] for _ in range(N)]

    max = 0
    result_num = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for y in range(N):
        for x in range(N):
            if L[y][x] != 0:
                dfs(y,x)
                result_num += 1

    print("#{} {} {}".format(tc+1, result_num, max))
