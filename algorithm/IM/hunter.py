def find(i, j):
    global cnt

    for k in range(8):
        for m in range(1, N):
            ny = i + dy[k] * m
            nx = j + dx[k] * m
            if 0 <= ny < N and 0 <= nx < N:
                if L[ny][nx] == 0:
                    break
                elif L[ny][nx] == 2:
                    cnt += 1
                    L[ny][nx] = 5
                # for m in range(2, N):
                #     my = i + m * dy[k]
                #     mx = j + m*dx[k]
                #     if 0 <= my < N and 0 <= mx < N:
                #         if L[my][mx] == 0 or L[my][mx] == 1:
                #             break
                #         elif L[my][mx] == 2:
                #             cnt += 1
                #             L[my][mx] = 5





import sys
from pprint import pprint
sys.stdin = open("hunter.txt")

N = int(input())
L = []
for i in range(N):
    L.append(list(map(int, input())))


dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
cnt = 0

for i in range(N):
    for j in range(N):
        if L[i][j] == 1:
            find(i, j)
print(cnt)

