N = int(input())
arr = list(map(int, input().split()))

def Qsort(start, end):
    if start >= end:
        return
    p, t = end, start
    for L in range(start, end):
        if arr[L] < arr[p]:
            arr[L], arr[t] = arr[t], arr[L]
            t += 1
    arr[p], arr[t] = arr[t], arr[p]
    Qsort(start, t-1) # 왼쪽영역을 다시 콜한다
    Qsort(t+1, end) # 오른쪽영역을 다시 콜한다

Qsort(0, N-1)
print(*arr)