import sys
sys.stdin = open("도자기.txt")

def DFS(start, cnt):
    global sol
    if cnt == M:
        # for i in range(cnt):
        #     print(rec[i], end=' ')
        # print()
        sol+=1
        return
    back = 0
    for i in range(start, N):   # 재료
        if back == arr[i]:
            continue
        # if rec[cnt] == arr[i]:  # 같은 재료이면 스킵
        #     continue
        # rec[cnt]=arr[i]
        back=arr[i]
        DFS(i+1, cnt+1)
    rec[cnt] = 0

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())    # N:흙종류, M:흙을섞을수있는개수
    arr = list(map(int, input().split()))
    arr.sort()

    rec = [0]*N
    sol = 0
    DFS(0, 0)
    print(sol)


