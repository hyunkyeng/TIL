import sys
sys.stdin = open("로봇.txt")

def BFS():
    dr = (0, 0, 0, 1, -1)
    dc = (0, 1, -1, 0, 0)
    turn = [(0, 0), (4, 3), (3, 4), (1, 2), (2, 1)]  #동서남북1234별 왼쪽턴0열, 오른쪽턴1열
    que = [(sr, sc, sdir, 0)]   # 행, 열, 방향, 명령횟수
    chk[sdir][sr][sc] = 1

    #1. 시작점을 큐에 저장(방문표시)
    while que:
        # 2.큐에서 데이터 읽기
        r, c, dir, cnt = que.pop(0)
        if r==er and c==ec and dir==edir:
            return cnt
        for i in range(1, 4): # go 1,2,3
            nr = r + dr[dir]*i
            nc = c + dc[dir]*i
            if nr < 0 or nr >= R or nc < 0 or nc >= C:  # 맵 범위 벗어나면
                break
            if arr[nr][nc] == 1:        # 벽이면
                break
            if chk[dir][nr][nc]:        # 길이지만 방문했다면 스킵
                continue
            que.append((nr, nc, dir, cnt+1))
            chk[dir][nr][nc] = 1
        for i in range(2):  # 왼쪽턴 0열, 오른쪽턴 1열
            ndir = turn[dir][i]
            if chk[ndir][r][c]:
                continue
            que.append((r, c, ndir, cnt+1))
            chk[ndir][r][c] = 1

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
chk = [[[0]*C for _ in range(R)] for _ in range(R)]
sr, sc, sdir = map(int, input().split())
er, ec, edir = map(int, input().split())
sr, sc = sr-1, sc-1
er, ec = er-1, ec-1

print(BFS())
