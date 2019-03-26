import sys
sys.stdin = open("베이비진게임.txt")

def check(x):
    win = 0

    for i in range(len(x)-2):
        if x[i] >= 3:
            win += 1
        if x[i] >= 1 and x[i+1] >= 1 and x[i+2] >= 1:
            win += 1
    return win



T = int(input())
for tc in range(T):
    data = list(map(int, input().split()))
    a = [0 for _ in range(10)]
    b = [0 for _ in range(10)]
    a_cnt, b_cnt = 0, 0
    result = 0

    for i in range(0, len(data), 2):
        a[data[i]] += 1
        a_cnt += 1
        if a_cnt >= 3:
            win = check(a)
            if win > 0:
                result = 1
                break
        b[data[i+1]] += 1
        b_cnt += 1
        if b_cnt >= 3:
            win = check(b)
            if win > 0:
                result = 2
                break
    print('#{} {}'.format(tc + 1, result))



