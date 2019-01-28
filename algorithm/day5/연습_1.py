#문자열 뒤집기

# 첫번째 방법

def my_strrev(ary):
    str = list(ary)
    for i in range(len(str)//2):
        t = ary[i]
        str[i] =str[len(str)-1-i]
        str[len(ary) - 1 -i ] = t
    ary = "".join(str)
    return ary

ary = "abcde"
ary = my_strrev(ary)
print(ary)



# 두번째 방법
s = "Reverse this strings"
s = s[-1:0:-1]
print(s)