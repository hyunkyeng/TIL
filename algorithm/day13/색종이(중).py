import sys
sys.stdin = open("색종이(중).txt")


N = int(input())
G = [[0 for _ in range(102)] for _ in range(102)]
length = 0

for n in range(N):
    y, x = list(map(int, input().split()))
    for i in range(y, y+10):
        for j in range(x, x+10):
            G[i][j] = 1

for i in range(102):  # 벽처리를 안하고 더 크게 잡는다.
    for j in range(102):
        if G[i][j] == 1:
                if G[i-1][j] == 0:  #상
                    length += 1
                if G[i][j-1] == 0:  #좌
                    length += 1
                if G[i+1][j] == 0:  #하
                    length += 1
                if G[i][j+1] == 0:  #우
                    length += 1


print(length)



