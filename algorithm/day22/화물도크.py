import sys
sys.stdin = open("화물도크.txt")

def out(data):
    global result
    s , e = data

    for i in range(s, e):
        if visited[i]:
            return
    for i in range(s, e):
        visited[i] = 1
    result += 1



T = int(input())
for tc in range(T):
    N = int(input())    # N : 신청서 수
    data = [ list(map(int, input().split())) for _ in range(N)]
    visited = [ 0 for _ in range(25)]
    result = 0


    data.sort(key=lambda x:x[1])

    for i in data:
        out(i)
    print('#{} {}'.format(tc+1, result))