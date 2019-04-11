import sys
sys.stdin = open("농작물.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    result = 0

    k = N//2
    start, end = k, k
    for i in range(N):
        for j in range(start, end + 1):
            result += data[i][j]
        if i+1 <= N//2:
            start, end = start-1, end+1
        else:
            start, end = start+1, end-1




    print('#{} {}'.format(tc+1, result))