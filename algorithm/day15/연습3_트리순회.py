#전위
def preorder(node):
    if node != 0:
        print("{}".format(node), end = " ")
        preorder(tree[node][0])
        preorder(tree[node][1])
#중위
def inorder(node):
    if node !=0:
        inorder(tree[node][0])
        print("{}".format(node), end = " ")
        inorder(tree[node][1])
#후위
def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print("{}".format(node), end = " ")

def printTree():
    for i in range(1, V+1):
        print("%2d %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2]))


import sys
sys.stdin = open("연습3_트리순회.txt")

V, E = map(int, input().split())
tree = [[0 for _ in range(3)] for _ in range(V+1)]
temp = list(map(int, input().split()))



for i in range(E):
    n1 = temp[i * 2]
    n2 = temp[i * 2 + 1]
    if not tree[n1][0]:     #값이 비어있으면 왼쪽값을 넣는다
        tree[n1][0] = n2
    else:       #왼쪽값이 채워져 있으면 오른쪽 값을 넣는다
        tree[n1][1] = n2
    tree[n2][2] = n1   #부모값 채우기

printTree()

print("전위 순회: ", end='')
preorder(1)
print()

print("중위 순회: ", end='')
inorder(1)
print()

print("후위 순회: ", end='')
postorder(1)
print()