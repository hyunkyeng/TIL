import sys
sys.stdin = open("그래프칠하기.txt")

def check(n, color):
    # 현재노드와 연결된 노드의 중복색상 여부 체크
    for i in range(n):  # 연결된 노드(열)
        if arr[n][i] and rec[i]==color: # 연결된노드와 같은색이면 실패
            return 0
    return 1


def DFS(n):
    global flag
    if n>=N:
        flag = 1
        return
    # 현재 노드에게 1~M색상을 칠해보는 경우의 수
    for i in range(1, M+1):
        if check(n, i):    # 현노드에게 칠할 수 있으면 기록하고 다음 노드로
            rec[n] = i  # 색상기록
            DFS(n+1)
            if flag:
                return


N, M = map(int, input().split())
rec = [0]*N    # 색상기록
arr = []    #인접행렬
for i in range(N):  # 0행 0열부터 사용
    arr.append(list(map(int, input().split())))
# print(arr)

flag = 0
DFS(0)  # 첫번째 노드부터 시작
if flag:
    for i in range(N):
        print(rec[i], end=' ')
else:
    print(-1)   # 실패