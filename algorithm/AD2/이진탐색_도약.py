import sys
sys.stdin = open("이진탐색_도약.txt")

def upperSearch(s, e, data):
    sol = -1
    while s <= e:
        m = (s+e)//2
        if arr[m] < data:
            s = m + 1
            sol = m
        else:
            e = m - 1
    return sol

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
# print(arr)
cnt = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        start = arr[j] + (arr[j] - arr[i])
        end = arr[j] + (arr[j] - arr[i]) * 2
        cnt += upperSearch(j, N-1, end+1) - upperSearch(j, N-1, start)

print(cnt)