import sys
sys.stdin = open("장기(백준).txt")

def bfs():
    # global r2, c2

    flag = 0
    que = []

    que.append((r1, c1, 0))
    data[r1][c1] = 1
    while que:
        x, y, count = que.pop(0)

        if x == r2 and y == c2:
            return count

        for i in range(8):
            flag = 0
            nx = x + dx[i]
            ny = y + dy[i]


            if nx < 0 or nx >= 10 or ny < 0 or ny >= 9:
                continue
            for j in wall[i]:
                if r2 == x + j[0] and c2 == y + j[1]:
                    flag = 1
            if flag == 0:
                data[nx][ny] = 1
                que.append((nx, ny, count + 1))

    return -1


r1, c1 = map(int, input().split())  # 상 위치
r2, c2 = map(int, input().split())  # 왕 위치
data = [[0 for _ in range(9)] for _ in range(10)]
data[r2][c2] = 9
# print(data)

dx = [-3, -3, -2, 2, 3, 3, 2, -2]
dy = [-2, 2, 3, 3, 2, -2, -3, -3]

wall = [[[-1, 0], [-2, -1]], [[-1, 0], [-2, 1]], [[0, 1], [-1, 2]], [[0, 1], [1, 2]], [[1, 0], [2, 1]],
        [[1, 0], [2, -1]], [[0, -1], [1, -2]], [[0, -1], [-1, -2]]]

print(bfs())

# print(data)