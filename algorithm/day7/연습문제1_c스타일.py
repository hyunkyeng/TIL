# Q. 스택을 구현해 봅시다.
# 구현한 스택을 이용하여 3개의 데이터를 스택에 저장하고 다시 3번 꺼내서 출력해 봅니다.

SIZE = 100
stack = [0] * SIZE
top = -1
def push(item):
    global top
    if top > SIZE - 1:
        return
    else:
        top += 1
        stack[top] = item

def pop():
    global top
    if top == -1:
        print("Stack is Empty!")
        return 0;
    else:
        result = stack[top]
        top -= 1
        return result


push(1)
push(2)
push(3)
print(pop())