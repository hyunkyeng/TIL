# Q. str()함수를 사용하지 않고, itoa()를 구현해 봅시다.

def itoa(x):
    str = list()
    y = 0
    while True:
        y = x % 10
        str.append(chr(y + ord('0')))
        x //= 10
        if x == 0:
            break

    str.reverse()
    str = "".join(str)
    return str

x = 123
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))
str2 = str(x)
print(str2, type(str2))