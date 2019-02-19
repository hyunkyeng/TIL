import sys
sys.stdin = open("Forth.txt")

def cal(L):
    for i in range(len(L)):
        if L[i].isdigit():
            stack.append(L[i])
        elif L[i] == '.':
            if len(stack) == 1:
                return stack[0]
            else:
                return 'error'
        else:
            if len(stack) < 2:
                return 'error'
            else:
                if L[i] == '+':
                    x = int(stack.pop(-2)) + int(stack.pop(-1))
                    stack.append(x)
                elif L[i] == '-':
                    x = int(stack.pop(-2)) - int(stack.pop(-1))
                    stack.append(x)
                elif L[i] == '*':
                    x = int(stack.pop(-2)) * int(stack.pop(-1))
                    stack.append(x)
                elif L[i] == '/':
                    x = int(int(stack.pop(-2)) / int(stack.pop(-1)))
                    stack.append(x)


T = int(input())
for tc in range(T):
    L = list(input().split())
    stack = []

    print(f'#{tc+1} {cal(L)}')