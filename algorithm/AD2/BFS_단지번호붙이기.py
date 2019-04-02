import sys
sys.stdin = open("단지번호붙이기.txt")

def check(y, x):
    global cnt, data
    data[y][x] = 0
    cnt += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if data[ny][nx] == 1:
                check(ny, nx)


N = int(input())
data = [list(map(int, input())) for _ in range(N)]
# print(data)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
result = []
for y in range(N):
    for x in range(N):
        if data[y][x] == 1:
            check(y, x)
            result.append(cnt)
        cnt = 0
print(len(result))
result.sort()
for i in result:
    print(i)