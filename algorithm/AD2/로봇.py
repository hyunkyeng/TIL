import sys
sys.stdin = open("로봇.txt")

def BFS():
    dr = (0, 0, 0, 1, -1)
    dc = (0, 1, -1, 0, 0)
    turn = [(0, 0), (4, 3), (3, 4), (1, 2), (2, 1)]  #동서남북 왼쪽턴, 오른쪽턴
    que = []

    #1. 시작점을 큐에 저장(방문표시)
    while que:
        # 2.큐에서 데이터 읽기
        for i in range(1, 4): # go 1,2,3

        for i in range(2):  # turn left, right

R, C = map(int(input().split()))
arr = [list(map(int, input().split())) for _ in range(R)]
chk = []
