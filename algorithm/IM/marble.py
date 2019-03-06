def dir(y, x):
    global L, direc
    while direc <= len(direction) - 1:
        ny = y + dy[direction[direc]]
        nx = x + dx[direction[direc]]
        if 0 <= nx < r and 0<= ny <c and L[ny][nx] != 1:
            L[ny][nx] = 9
            y = ny
            x = nx
        else:
            direc += 1


import sys
from pprint import pprint
sys.stdin = open("marble.txt")

r, c = map(int, input().split())    # r:가로, c:세로
L = []
for i in range(c):
    L.append(list(map(int, input())))
N = int(input())
direction = list(map(int, input().split()))     #방향정보


dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]

direc = 0   #방향 틀때마다 얘를 1씩 증가시켜서 주어진 방향정보로 가게 한다
cnt = 0

for y in range(c):
    for x in range(r):
        if L[y][x] == 2:
            result_L = dir(y, x)

for y in range(c):
    for x in range(r):
        if L[y][x] == 9 or L[y][x] == 2:
            cnt += 1

print(cnt)
