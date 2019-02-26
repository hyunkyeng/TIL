def bfs(x, y):
    global G
    queue = []
    queue.append([x,y])
    visited[y][x] = 1

    while len(queue) != 0:
        t = queue.pop(0)
        for i in range(4):
            new_x = t[0] + dx[i]
            new_y = t[1] + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                if G[new_y][new_x] == 2:
                    return visited
                elif G[new_y][new_x] == 0 and visited[new_y][new_x] == 0:
                    queue.append([new_x,new_y])
                    visited[new_y][new_x] = visited[t[1]][t[0]] + 1


import sys
sys.stdin = open("미로의거리.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    G = [list(map(int, input())) for _ in range(N)]
    # print(G)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    result = []

    start_x, start_y = 0, 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for y in range(N):
        for x in range(N):
            if G[y][x] == 3:
                start_x = x
                start_y = y
                break
            if G[y][x] == 2:
                end_x = x
                end_y = y

    visited = bfs(start_x, start_y)

    if visited:
        for i in range(4):
            x = end_x + dx[i]
            y = end_y + dy[i]
            if 0 <= x < N and 0 <= y < N:
                result.append(visited[y][x])
        print(f'#{tc+1} {max(result)-1}')
    else:
        print(f'#{tc+1} 0')
