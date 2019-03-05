def inorder(n):
    global idx, tree
    if n <= N:
        inorder(2 * n)
        tree[n] = idx
        idx += 1
        inorder(2 * n + 1)
    return tree


import sys
sys.stdin = open("이진탐색.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    tree = [0] * (N+1)
    idx = 1

    result = inorder(1)
    print("#{} {} {}".format(tc+1, tree[1], tree[N//2]))