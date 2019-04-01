import sys
sys.stdin = open("전기카트.txt")

def perm(n, k):
    if n == k:
        route.append(a[:])
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]


T = int(input())

for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    route = []
    min_distance = 1000000

    a = [ i for i in range(2, N+1)]

    perm(N-1, 0)

    for i in range(len(route)):
        route[i] = [1] + route[i] + [1]

    for i in range(len(route)):
        distance = 0
        for j in range(N):
            distance += data[route[i][j]-1][route[i][j+1]-1]
            if distance > min_distance:
                break
        if min_distance > distance:
            min_distance = distance
    print('#{} {}'.format(tc+1, min_distance))
