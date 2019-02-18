


str = "2+3*4/5"
stack = []

for i in range(len(str)):
    if str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/':
        stack.append(str[i])
    else:
        print(str[i], end="")

while len(stack) != 0:
    print(stack.pop(), end='')









