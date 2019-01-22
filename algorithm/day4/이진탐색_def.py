import sys
sys.stdin = open("이진탐색_input.txt")

T = int(input())

def binary(x, P):
    l = 1
    r = P
    count = 0
    while True:
        c = (l + r) // 2
        count += 1
        if c == x:
            return count
            break
        if x > c:
            l = c
        else:
            r = c


for tc in range(T):
    P, Pa, Pb = map(int, (input().split()))
    countA = binary(Pa, P)
    countB = binary(Pb, P)


    if countA > countB:
        print(f'#{tc+1} B')
    if countA < countB:
        print(f'#{tc+1} A')
    if countA == countB:
        print(f'#{tc+1} 0')
