import sys
sys.stdin = open("이진탐색_숫자카운팅.txt")

def upperSearch(s, e, data):
    sol = -1
    while s <= e:
        m = (s+e) // 2
        if arr[m] < data:   #data보다 작은 값중에서 가장 큰값의 위치 찾기
            s = m+1         #data보다 작으면 오른쪽 영역 재탐색
            sol = m
        else:
            e = m-1     #data보다 크거나 같으면 왼쪽영역 재탐색
    return sol          #못찾으면 -1리턴

N = int(input())
arr = list(map(int, input().split()))
T = int(input())
tarr = list(map(int, input().split()))
for i in range(T):
    print(upperSearch(0, N-1, tarr[i]+1) - upperSearch(0, N-1, tarr[i]), end=" ")

