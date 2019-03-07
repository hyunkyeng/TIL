import sys
import math
sys.stdin = open("town_in_circle.txt")

def find(i, j):
    global max
    for y in range(N):
        for x in range(N):
            if L[y][x] == 1:
                d = (j-x)**2 + (i-y)**2
                if d > max:
                    max = d
    return max

N = int(input())
L = []
max = 0

for i in range(N):
    L.append(list(map(int, input())))

for i in range(N):
    for j in range(N):
        if L[i][j] == 2:
            find(i, j)

print(math.ceil(math.sqrt(max)))
