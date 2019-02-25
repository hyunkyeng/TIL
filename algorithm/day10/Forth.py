import sys
sys.stdin = open("Forth.txt")

def cal(L):
    for i in range(len(L)):
        if L[i].isdigit():
            stack.append(L[i])
        elif L[i] == '.':
            if len(stack) == 1:   # 계산다했을 때 1 개 남으면 출력 1개가 아니면 에러
                return stack[0]
            else:
                return 'error'
        else:
            if len(stack) < 2:   #연산자가 나왔을때 숫자가 2개보다 작으면 에러
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
                    x = int(int(stack.pop(-2)) // int(stack.pop(-1)))   #나누어떨어진다고 했으므로 몫으로 계산
                    stack.append(x)


T = int(input())
for tc in range(T):
    L = list(input().split())
    stack = []

    print(f'#{tc+1} {cal(L)}')