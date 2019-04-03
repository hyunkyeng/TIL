import sys
sys.stdin = open("NQUEEN.txt")

dr = [-1, -1, -1]
dc = [-1, 0, 1]

def check(r, c):
    # 현재 좌표에 퀸을 놓을 수 있는지 여부 체크
    for i in range(3):  # 3방향
        for k in range(1, N):   # 1배, 2배,,, 증감치의 배수 계산
            nr = r + dr[i]*k
            nc = c + dc[i]*k
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                break
            if arr[nr][nc] == 1:
                return 0        # 놓을 수 없음 실패
    return 1    # 퀸을 놓을 수 있음 성공

def DFS(n):     # 현재 행에서 모든 열에 퀸을 놓아보는 경우
    global sol
    if n>=N:
        sol += 1
        return
    for i in range(N):
        if chk1[i]:      # 세로 방향 체크
            continue
        if chk2[n+i]:      # 오른쪽 대각선 방향 체크
            continue
        if chk3[(N-1)-(n-i)]:      # 왼쪽 대각선 방향체크
            continue
        chk1[i] = chk2[n+i] = chk3[(N-1)-(n-i)] = 1
        DFS(n+1)
        chk1[i] = chk2[n+i] = chk3[(N-1) - (n-i)] = 0

    # # 맵이 크지 않으면 for 문으로도 풀 수 있다.
    # for i in range(N):  # 열
    #     if check(n, i):     # 퀸을 놓을 수 있으면
    #         arr[n][i] = 1   # 퀸 놓기
    #         DFS(n+1)
    #         arr[n][i] = 0   # 퀸 빼기


N = int(input())
arr = [[0]*N for _ in range(N)]
chk1 = [0]*N
chk2 = [0]*N*2
chk3 = [0]*N*2
sol = 0
DFS(0)  # 0행부터 시작
print(sol)