import sys
sys.stdin = open("miro.txt")

def direc():





N = int(input())
L = []
for i in range(N):
    L.append(list(input()))
direction = list(map(int, input().split()))  # 1:아래,2:왼쪽,3:위,4:오른쪽
print(L)
print(direction)

dx = [0, 0, -1, 0, 1]
dy = [0, 1, 0, -1, 0]

for i in range(N):
    for j in range(N):

