def SearchTree(n):
    global count
    if n != 0:
        count += 1
        SearchTree(tree[n][0])
        SearchTree(tree[n][1])
    return count

import sys
sys.stdin = open("서브트리.txt")

T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(E+2)]
    count = 0

    for i in range(E):
        n1 = temp[i*2]
        n2 = temp[i*2 + 1]
        if not tree[n1][0]:     #값이 비어있으면 왼쪽 값을 넣는다
            tree[n1][0] = n2
        else:   #왼쪽값이 채워져 있으면 오른쪽 값을 넣는다
            tree[n1][1] = n2
        tree[n2][2] = n1    #부모값 채우기

    print("#{} {}".format(tc+1, SearchTree(N)))