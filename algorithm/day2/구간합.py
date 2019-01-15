import sys
sys.stdin = open("구간합_input.txt")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))
    # print(number)
    sum_number = 0
    L = []
    max_number = 0
    min_number = 99999999999
    for i in range(N-M+1):
        for j in range(M):
            sum_number += number[i + j]
        L.append(sum_number)
        sum_number = 0
        for i in range(len(L)):
            if max_number < L[i]:
                max_number = L[i]
            if min_number > L[i]:
                min_number = L[i]
    print(f"#{test_case+1} {max_number - min_number}")
