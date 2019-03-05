import sys
sys.stdin = open("폭탄돌리기.txt")

k = int(input())    # 처음에 폭탄을 가지고 있는 사람
N = int(input())    # 문제 수
total = 0
for i in range(N):
    T, result = map(str, input().split())
    T = int(T)
    if result == 'T':
        total += T
        if total > 210:
            print(k)
            break
        k += 1
        if k > 8:
            k = k % 8
    else:
        total += T
        if total > 210:
            print(k)
            break
if total < 210:
    print(k)