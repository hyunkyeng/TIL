import sys
sys.stdin = open("숫자카드_input.txt")


T = int(input())
for test_case in range(T):
    N = int(input())
    L = list(map(int, input()))
    c = [0] * 10
    max_number = c[0]
    index_number = 0
    for i in range(len(L)):
        c[L[i]] += 1
    for j in range(10):
        if max_number <= c[j]:
            max_number = c[j]
            index_number = j
    print(c)
    print(f'#{test_case+1} {index_number} {max_number}')



