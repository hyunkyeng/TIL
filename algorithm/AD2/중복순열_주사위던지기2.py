import sys
sys.stdin = open("중복순열_주사위던지기2.txt")

# 중복순열
def DFS(n):
    if n > N:
        for i in range(1, N+1):
            print(rec[i], end=" ")
        print()
        return
    for i in range(1, 7):
        rec[n] = i
        DFS(n+1)

# 중복 배제 순열 ( 눈의 중복을 배제한 순열 )
def DFS2(n):
    if n > N:
        for i in range(1, N+1):
            print(rec[i], end=" ")
        print()
        return
    for i in range(1, 7):   # 눈
        if chk[i]:
            continue
        chk[i] = 1      # 눈 사용 체크
        rec[n] = i
        DFS2(n+1)
        chk[i] = 0      # 눈 사용체크 해제

# 눈의 합이 M인 경우만 인쇄
def DFS3(n, nsum):
    if n > N:
        if nsum == M:
            for i in range(1, N+1):
                print(rec[i], end=' ')
            print()
        return
    for i in range(1, 7):
        rec[n] = i
        DFS3(n+1, nsum+i)


N, M = map(int, input().split())
rec = [0]*8     # 주사위별 눈 기록 배열
chk = [0]*7     # 눈 사용여부 체크배열

DFS3(1, 0)      # 1번 주사위부터 시작