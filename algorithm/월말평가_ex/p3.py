import sys
sys.stdin = open("p3.txt")

def check(a):
    flag = []
    global summ
    k = 0
    flag.append(a)
    k += 1
    for j in range(N):
        if j not in flag:
            summ += data[k][j]
            flag.append(j)
            k += 1
            for z in range(N):
                if z not in flag:
                    summ += data[k][z]
                    flag.append(z)
    if k == 3:
        return summ



T = int(input())
for tc in range(T):
    N = int(input())
    cookie = list(map(int, input().split()))
    robot = list(map(int, input().split()))


    data = [[0]*N for _ in range(N)]
    # print(data)


    for i in range(0, len(robot)//2):
        rx = robot[2*i]
        ry = robot[2*i +1]
        for j in range(0, len(cookie)//2):
            cx = cookie[2*j]
            cy = cookie[2*j +1]

            data[i][j] = abs(rx - cx) + abs(ry-cy)
    # print(data)
    L = []
    for i in range(N):
        summ = data[0][i]
        check(i)
        L.append(summ)
    print('#{} {}'.format(tc+1, min(L)))







