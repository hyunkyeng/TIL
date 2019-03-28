import sys
sys.stdin = open("토마토.txt")

def BFS():
    que = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    zero = 0    # 0의 개수 카운트
    r, c, day = 0, 0, 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 1:  # 익은 토마토 자리를 모두 시작점으로 큐에저장
                que.append((i, j, 0))
            elif arr[i][j] == 0:
                zero += 1
    if zero == 0:   #모두 익힌 상태라면 리턴
        return 0
    while que:
        r, c, day = que.pop(0)  # 2.큐에서 데이타 읽기(현재좌표)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr<0 or nr>=R or nc<0 or  nc>=C:
                continue
            if arr[nr][nc] == 0:    # 안익은 토마토라면
                que.append((nr, nc, day+1))
                arr[nr][nc] = 1     # 맵에 방문표시
                zero -= 1   # 익혀가면서 차감
    if zero:
        return -1   # 모두 못익힌 상태라면 -1 리턴
    else:
        return day  # 모두 익힌 상태하면 최소일자를 리턴

C, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
print(BFS())