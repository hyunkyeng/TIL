import sys
sys.stdin = open("색칠하기_input.txt")

T = int(input())
for tc in range(T):
    count = 0
    N = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        if color == 1:
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    arr[r][c] += 1
        if color == 2:
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    arr[r][c] += 2

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == 3:
                count += 1
    print(f'#{tc+1} {count}')




        # for x in range(arr):
        #     for y in range(arr[x]):
        #         if r1 < x < r2:
        #             arr[x] += color
        #         if