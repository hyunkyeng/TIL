
def search():
    count_x = 0
    count_y = 1
    L = []
    for y in range(N):
        for x in range(N):
            if G[y][x] != 0:
                count_x += 1
                G[y][x] = 0
                new_y = y
                # for i in range(1, N-new_y):
                #     if G[y+i][x] != 0:
                #         count_y += 1
                #         G[y+i][x] = 0

            else:
                if count_y != 0 or count_x != 0:
                    L.append([count_y, count_x])
                count_x, count_y = 0, 0

    print(L)
    print(len(L), end = " ")
    sort_L = sorted(L)
    result_L = [y for x in sort_L for y in x]
    for i in range(len(result_L)):
        print(result_L[i], end = " ")
    return ""





import sys
sys.stdin = open("행렬찾기.txt")

T = int(input())
for tc in range(1):
    N = int(input())    # N*N 행렬
    G = [list(map(int, input().split())) for _ in range(N)]
    print(G)

    print(search())
