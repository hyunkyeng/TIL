import sys
sys.stdin = open("장기.txt")

def bfs():

    que = [(sy, sx, 0)]

    while que:
        y, x, count = que.pop(0)
        if y == ey and x == ex:
            return count
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < Y and 0 <= nx < X:
                que.append(ny, nx, count+1)




Y, X = map(int, input().split())
sy, sx, ey, ex = map(int, input().split())
sy -= 1
sx -= 1
ey -= 1
ex -= 1


dx = [-1, 1, 2, 2, 1, -1, -1, -2]
dy = [-2, -2, -1, 1, 2, 2, 1, -1]

print(bfs())