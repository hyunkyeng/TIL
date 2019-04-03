import sys
sys.stdin = open("양팔저울.txt")

def DFS(n, Lsum, Rsum):
    global sol
    if sol:     # 가지치기
        return
    if n >= CN:
        if Lsum == Rsum:    # 양쪽저울무게가 같으면 성공
            sol = 1
        return
    # 현재 추를 사용하거나(왼쪽, 오른쪽저울에 사용) 사용하지 않기
    DFS(n+1, Lsum+chu[n], Rsum) # 현재 추를 왼쪽에 올리기
    DFS(n+1, Lsum, Rsum+chu[n])  # 현재 추를 오른쪽에 올리기
    DFS(n+1, Lsum, Rsum)  # 현재 추를 사용하지 않기



CN = int(input())
chu = list(map(int, input().split()))
BN = int(input())
ball = list(map(int, input().split()))
rec = [0] * CN      # 기록배열
for i in range(BN):
    sol = 0
    DFS(0, ball[i], 0)  # 0번추부터시작, 왼쪽저울무게 구슬을 초기값으로, 오른저울무게 0
    if sol:
        print('Y')
    else:
        print('N')