import sys
sys.stdin = open("로봇과자먹기.txt")


def DFS(n, nsum):
    global nmin
    if nsum > nmin:     # 가지치기
        return
    if n >= N:
        if nsum < nmin:
            nmin = nsum
        return
    for i in range(N):      # 과자 열
        if chk[i]:
            continue
        chk[i] = 1
        rec[n] = data[n][i]             # 거리기록
        DFS(n+1, nsum + data[n][i])
        chk[i] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    cookie = list(map(int, input().split()))
    robot = list(map(int, input().split()))
    chk = [0] * N   # 과자 중복여부 체크 배열
    rec = [0] * N   # 로봇별 먹은 과자의 거리 기록배열

    data = [[0]*N for _ in range(N)]
    # print(data)


    for i in range(0, len(robot)//2):
        rx = robot[2*i]
        ry = robot[2*i +1]
        for j in range(0, len(cookie)//2):
            cx = cookie[2*j]
            cy = cookie[2*j +1]

            data[i][j] = abs(rx - cx) + abs(ry-cy)
    # print(data)

    nmin = 1000000
    DFS(0, 0)
    print(nmin)
