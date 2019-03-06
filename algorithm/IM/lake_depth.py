def depth(i, j):
    for m in range(1, N):
        for k in range(4):
            if 0 <= i+m*dx[k] < N and 0 <= j+m*dy[k] < N:
                if lake[i+m*dx[k]][j+m*dy[k]] == 0:
                    return m


import sys
sys.stdin = open("lake_depth.txt")

N = int(input())
lake = []
sum = 0
for i in range(N):
    lake.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(N):
    for j in range(N):
        if lake[i][j] == 1:
            sum += depth(i, j)

print(sum)

