import sys
sys.stdin = open("더하기.txt")

def DFS(no, nsum):
    global flag
    if nsum == K:
        flag = 1
        return
    if nsum > K or flag:    #가지치기
        return
    if no>=N:
        return
    rec[no] = arr[no]
    DFS(no+1, nsum+arr[no])
    rec[no] = 0
    DFS(no+1, nsum)

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    rec = [0]*N
    flag = 0
    DFS(0, 0)
    if flag:
        print('YES')
    else:
        print('NO')