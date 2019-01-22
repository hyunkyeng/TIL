import sys
sys.stdin = open("달팽이숫자_input.txt")

T = int(input())

for tc in range(1):
    N = 3
    L = list(range(1, N*N))
    arr = [[ 0 for _ in range(N)] for _ in range(N)]

    for y in range(len(arr[0])):
        for i in range(N):
            arr[0][y] = L[i]
            y = y+1



    # for x in range(len(arr)):
    #     for y in range(len(arr[x])):
    #         for i in range(N):
    #             arr[x][y] = L[i]
    #             y = y+1

    print(arr)



