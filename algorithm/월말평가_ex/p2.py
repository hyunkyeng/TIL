import sys
sys.stdin = open("p2.txt")

def check():
    L = []
    #1구역
    cnt = 0
    for i in range(y):
        for j in range(x1):
            cnt += data[i][j]
    L.append(cnt)
    #2구역
    cnt = 0
    for i in range(y):
        for j in range(x1, x2):
            cnt += data[i][j]
    L.append(cnt)
    #3구역
    cnt = 0
    for i in range(y):
        for j in range(x2, X):
            cnt += data[i][j]
    L.append(cnt)
    #4구역
    cnt = 0
    for i in range(y, Y):
        for j in range(x1):
            cnt += data[i][j]
    L.append(cnt)
    #5구역
    cnt = 0
    for i in range(y, Y):
        for j in range(x1, x2):
            cnt += data[i][j]
    L.append(cnt)
    #6구역
    cnt = 0
    for i in range(y, Y):
        for j in range(x2, X):
            cnt += data[i][j]
    L.append(cnt)
    return L


T = int(input())
for tc in range(T):
    Y, X = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(Y)]
    # print(data)
    max_sum = 0
    summ = []

    for y in range(1,Y):
        for x1 in range(1,X):
            a = [y, x1]
            for x2 in range(x1+1, X):
                b = [y, x2]

                L = check()
                L.sort()
                # print(L)
                sum1 = abs(L[-1]-L[0])+abs(L[0]-L[1])+abs(L[1]-L[-1])
                summ.append(sum1)
                if max_sum < sum1:
                    max_sum = sum1
    # print(summ)
    print("#{} {}".format(tc+1, max_sum))


