def change(y , x):
    global G
    k = 1

    if G[y][x] == 1:
        for i in range(8):
            ny = y + k * dy[i]
            nx = x + k * dx[i]
            if 0 <= ny < N and 0 <= nx < N and G[ny][nx] == 2:
                k += 1
                while 0 <= y + k * dy[i] < N and 0 <= x + k * dx[i] < N:
                    if G[y + k * dy[i]][x + k * dx[i]] == 0:
                        break
                    # elif G[ny][nx] == 2:
                    #     pass
                    if G[y + k * dy[i]][x + k * dx[i]] == 1:
                        for l in range(1, k):
                            G[y + l * dy[i]][x + l * dx[i]] = 1
                        break
                    k += 1
            k = 1


    elif G[y][x] == 2:
        for i in range(8):
            ny = y + k * dy[i]
            nx = x + k * dx[i]
            if 0 <= ny < N and 0 <= nx < N and G[ny][nx] == 1:
                k += 1
                while 0 <= y + k * dy[i] < N and 0 <= x + k * dx[i] < N:
                    if G[y + k * dy[i]][x + k * dx[i]] == 0:
                        break
                    # elif G[ny][nx] == 1:
                    #     pass
                    elif G[y + k * dy[i]][x + k * dx[i]] == 2:
                        for l in range(1, k):
                            G[y + l * dy[i]][x + l * dx[i]] = 2
                        break
                    k += 1
            k = 1




import sys
sys.stdin = open("오셀로게임.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split()) # N:보드의한변, M:돌을 놓는 횟수

    G = [[0 for _ in range(N)] for _ in range(N)]
    G[N//2-1][N//2-1], G[N//2][N//2] = 2, 2
    G[N//2-1][N//2], G[N//2][N//2-1] = 1, 1

    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]

    black, white = 0, 0

    for i in range(M):
        # L.append(list(map(int, input().split())))
        x, y, color = map(int, input().split())
        x = x-1
        y = y-1
        G[y][x] = color
        change(y, x)

    for i in range(N):
        for j in range(N):
            if G[i][j] == 1:
                black += 1
            elif G[i][j] == 2:
                white += 1
    print('#{} {} {}'.format(tc+1, black, white))



