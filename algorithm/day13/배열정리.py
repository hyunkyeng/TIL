import sys
sys.stdin = open("배열정리.txt")


Y, X = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(Y)]


for y in range(Y):
    count = 0
    for x in range(X):
        if G[y][x] == 1:
            count += 1
            G[y][x] = count
        elif G[y][x] == 0:
            count = 0


for i in range(Y):
    for j in range(X):
        print(G[i][j], end=" ")
        if j == X-1:
            print()

