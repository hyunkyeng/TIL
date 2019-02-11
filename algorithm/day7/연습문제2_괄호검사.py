# Q. 괄호의 짝을 검사하는 프로그램을 작성해봅시다.
# 작성한 프로그램에서 다음 괄호 사용을 검사해봅시다.

s=[]

def push(item):
    s.append(item)
    return

def pop():
    return s.pop(-1)

def isEmpty():
    if len(s) == 0:
        return True
    else:
        return False

def check_matching(data):
    for i in range(len(data)):
        if data[i] == "(":
            push(data[i])
        elif data[i] == ")":
            if isEmpty():
                return False
            pop()

    # ((((((((((( ) 일 수도 있으니 아래 코드도 작성해야한다. 
    if not isEmpty():
        return False
    else:
        return True



print(check_matching('()()((()))'))
print(check_matching('((()((((()()((()())((())))))))))'))
