import sys
sys.stdin = open("jump.txt")

N = int(input())
L = []
cnt = 0
for i in range(N):
    L.append(int(input()))
    L.sort()

for i in range(N-1):    #처음 점프 하는 위치
    for j in range(i+1, N-1):    #두번째 점프하는 위치
        for k in range(j+1, N):   #두번 점프 후 도착하는 위치
            first = L[j] - L[i]
            second = L[k] - L[j]
            if first <= second and 2 * first >= second:
                cnt += 1


print(cnt)