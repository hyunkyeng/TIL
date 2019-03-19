import sys
sys.stdin = open('이진수2.txt')

T = int(input())
str = ''
for tc in range(T):
    N = float(input())

    print('#{}'.format(tc+1), end=" ")

    for i in range(1, 14):
        if N == 0:
            break
        if N - (1/2)**i >= 0:
            N = N - (1/2)**i
            str += '1'
        else:
            str += '0'
    if N > 0:
        print('overflow')
    else:
        print(str)
    str=''
