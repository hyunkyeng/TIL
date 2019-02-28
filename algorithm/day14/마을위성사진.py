import sys
sys.stdin = open("마을위성사진.txt")


N = int(input())
arr = [[0 for _ in range(N+2)] for _ in range(N+2)]

for i in range(1, N+1):
    arr[i][1:N] = list(map(int, input()))

def check(x, y, a):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    unduck=[]
    for i in range(4):
        unduck.append(a[x+dx[i]][y+dy[i]])
    return unduck

for i in range(100):
    for r in range(2, N):
        for c in range(2, N):
            if arr[r][c]:
                unduck=check(r, c, arr)
                if 0 in unduck:
                    arr[r][c] =1
                else:
                    arr[r][c] = min(unduck)+1

maxunduck=0
for r in range(N+2):
    for c in range(N+2):
        if maxunduck<arr[r][c]:
            maxunduck = arr[r][c]
print(maxunduck)