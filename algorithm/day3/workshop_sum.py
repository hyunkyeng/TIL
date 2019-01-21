import sys
sys.stdin = open("workshop_sum.txt")

T = 10
L = []
sum = 0
for test_case in range(T):
    L = []
    N = input()
    arr = [[0 for a in range(100)] for b in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    for x in range(len(arr)):
        sum = 0
        for y in range(len(arr[0])):
            sum += arr[x][y]
        # print(sum)
            L.append(sum)
    for y in range(len(arr)):
        sum = 0
        for x in range(len(arr[0])):
            sum += arr[x][y]
        L.append(sum)
    for x in range(len(arr)):
        sum = 0
        for y in range(len(arr[0])):
            if x == y:
                sum += arr[x][y]
            if x + y == len(arr[0]):
                sum += arr[x][y]
            L.append(sum)
    result = max(L)
    print(f'#{N} {result}')






