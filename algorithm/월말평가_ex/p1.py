import sys
sys.stdin = open("p1.txt")

def bfs(x, y, cnt):
    que = [(x, y, cnt)]
    data[y][x] = 1

    while que:
        x, y, cnt = que.pop(0)
        if x == tx and y == ty:
            return cnt
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                for j in wall[i]:
                    if x + j[0] == tx and y + j[1] == ty:
                        continue
                que.append((nx, ny, cnt+1))



T = int(input())
for tc in range(T):
    N = int(input())
    x, y, tx, ty = map(int, input().split())
    data = [[0]*N for _ in range(N)]

    dx = [-2, 2, 3, 3, 2, -2, -3, -3]
    dy = [-3, -3, -2, 2, 3, 3, 2, -2]

    wall = [[[0, -1], [-1, -2]], [[0, -1], [1, -2]], [[1,0], [2, -1]], [[1, 0], [2, 1]],
            [[0, 1], [1, -2]], [[0, 1], [-1, 2]], [[-1, 0], [-2, 1]], [[-1, 0], [-2, -1]]]

    print("#{} {}".format(tc+1, bfs(x, y, 0)))
