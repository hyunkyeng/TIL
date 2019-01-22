import sys
sys.stdin = open("이진탐색_input.txt")

T = int(input())

for tc in range(T):
    P, Pa, Pb = map(int, (input().split()))
    l = 1
    r = P
    count = 0
    while True:
        c = (l + r) // 2
        count += 1
        if c == Pa:
            countA = count
            break
        if Pa > c:
            l = c
        else:
            r = c
    l = 1
    r = P
    count = 0
    while True:
        c = (l + r) // 2
        count += 1
        if c == Pb:
            countB = count
            break
        if Pb > c:
            l = c
        else:
            r = c
    if countA > countB:
        print(f'#{tc+1} B')
    if countA < countB:
        print(f'#{tc+1} A')
    if countA == countB:
        print(f'#{tc+1} 0')

