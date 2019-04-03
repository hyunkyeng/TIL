import sys
sys.stdin = open("미사일.txt")

# 현재 군함위치에서 반경이내 에너지 모두 차감
def clear(n):   # n:미사일 맞은 군함
    for i in range(N):  # i : 주변에 있는 군함
        temp = abs(arr[n][0]-arr[i][0]) + abs(arr[n][1]-arr[i][1])
        if temp <= R:   # 반경이내이면
            arr[i][2] -= P

# 현재 군함위치에서 반경이내 에너지 모두 복원
def update(n):
    for i in range(N):  # i : 주변에 있는 군함
        temp = abs(arr[n][0]-arr[i][0]) + abs(arr[n][1]-arr[i][1])
        if temp <= R:   # 반경이내이면
            arr[i][2] += P


# 현재 n 미사일을 모두 군함에 쏘아보는 경우의 수 시도
def DFS(n):
    global sol
    if n == M:
        cnt = 0     # 남아있는 군함의 개수
        for i in range(N):
            if arr[i][2] > 0:
                cnt += 1
        if cnt < sol:
            sol = cnt
        return
    for i in range(N):      # 군함
        if arr[i][2] <= 0:      # 단 군함이 침몰하지 않은 군함에만 시도
            continue
        clear(i)        # 현재 군함반경이내 모든 군함에너지 차감
        DFS(n+1)        # 다음 미사일로
        update(i)       # 현재 군함반경이내 모든 군함에너지 복원


N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

M, P, R = map(int, input().split())
sol = 16
# print(arr)
DFS(0)  # 0번 미사일부터 시작
print(sol)