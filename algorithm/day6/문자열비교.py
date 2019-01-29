import sys
sys.stdin = open("문자열비교_input.txt")

T = int(input())
for tc in range(T):
    a = input()    #찾는 문자
    b = input()
    i = j = 0
    count = 0

    while j < len(b):    #i, j 는 인덱스
        if a[i] != b[j]:
            i = -1
        i += 1
        j += 1

        if i == len(a):    #찾으면 count +1 하고 i는 다시 리셋
            count += 1
            i = 0

    print(f'#{tc+1} {count}')


