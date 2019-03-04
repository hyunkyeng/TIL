def inorder(n):
    if n != 0:
        inorder(firstChild[n])
        print("{}".format(alpha[n]), end="")
        inorder(secondChild[n])

import sys
sys.stdin = open("중위순회.txt")

T = 10
for tc in range(T):
    N = int(input())
    firstChild = [0] * (N+1)
    secondChild = [0] * (N+1)
    alpha = [0] * (N+1)
    for i in range(N):
        temp = list(input().split())
        # print(temp)
        addr = int(temp[0])
        ch = temp[1]
        alpha[addr] = ch
        if addr * 2 <= N:
            firstChild[addr] = int(temp[2])
            if addr * 2 + 1 <= N:
                secondChild[addr] = int(temp[3])

    print("#{}".format(tc+1), end=" ")
    inorder(1)
    print()