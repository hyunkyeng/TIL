import sys
sys.stdin = open("sum_input.txt")
T = 10
for tc in range(T):
    no = int(input())
    data = [[0 for _ in range(100)]for _ in range(100)]
    for i in range(100):  # 입력
        data[i] = list(map(int, input().split()))

    max = 0
    for i in range(100):  #row
        sum = 0
        for j in range(100):
            sum += data[i][j]
        if sum > max:
            max = sum

    for i in range(100):  # col
        sum = 0
        for j in range(100):
            sum += data[j][i]
        if sum > max:
            max = sum

    sum = 0
    for i in range(100):  # dia1
        sum += data[i][i]
    if sum > max:
        max = sum

    sum = 0
    for i in range(100):  # dia2
        sum += data[i][99-i]
    if sum > max:
        max = sum

    print("#{} {}".format(no, max))