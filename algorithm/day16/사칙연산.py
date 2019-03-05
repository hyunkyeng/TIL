def postorder(n):
    if n != 0:
        postorder(firstChild[n])
        postorder(secondChild[n])
        L.append(operater[n])
        if L[-1] == '+':
            L.pop()
            a = L.pop()
            L[-1] = L[-1] + a
        elif operater[n] == '-':
            L.pop()
            a = L.pop()
            L[-1] = L[-1] - a
        elif operater[n] == '*':
            L.pop()
            a = L.pop()
            L[-1] = L[-1] * a
        elif operater[n] == '/':
            L.pop()
            a = L.pop()
            L[-1] = L[-1] // a


        print("{}".format(operater[n]), end="")



import sys
sys.stdin = open("사칙연산.txt")

T = 10
for tc in range(1):
    N = int(input())
    firstChild = [0] * (N+1)
    secondChild = [0] * (N+1)
    operater = [0] * (N+1)
    L = []

    for i in range(N):
        temp = list(input().split())
        print(temp)
        addr = int(temp[0])
        oper = temp[1]
        operater[addr] = oper
        if addr * 2 <= N:
            firstChild[addr] = int(temp[2])
            secondChild[addr] = int(temp[3])

    print(firstChild)
    print(secondChild)
    print(operater)
    print(postorder(1))