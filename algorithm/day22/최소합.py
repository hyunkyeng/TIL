import sys
sys.stdin = open("최소합.txt")

def dfs(y, x, distance):
    global result
    if distance > result:
        return

    if y == N-1 and x == N-1:
        distance += data[y][x]
        if result > distance:
            result = distance

    for i in range(2):
        if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N:
            ny = y + dy[i]
            nx = x + dx[i]
            dfs(ny, nx, distance + data[y][x])


T = int(input())
for tc in range(T):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')

    dx = [1, 0] # 오른쪽, 아래
    dy = [0, 1]

    dfs(0, 0, 0)
    print('#{} {}'.format(tc+1, result))
