import sys
sys.stdin = open("종이붙이기.txt")

def paper(n):
    if n == 10:
        return 1
    if n == 20:
        return 3
    else:
        return paper(n-10) + 2 * paper(n-20)


T = int(input())
for tc in range(T):
    N = int(input())


    print(f'#{tc+1} {paper(N)}')