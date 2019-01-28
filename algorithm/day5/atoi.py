# int 쓰는 것을 구현.

def atoi(string):
    value = 0
    i = 0
    while ( i < len(string)):
        c = string[i]
        if c >= '0' and c <= '9':          # 아스키 코드 값으로 비교하는 것.
            digit = ord(c) - ord('0')    # ord : 아스키 코드로 변경해 주는 것
        else:
            break
        value = (value * 10) + digit;
        i += 1
    return value

a = '123'
print(type(a))
b = atoi(a)
print(type(b))
c = int(a)
print(type(c))