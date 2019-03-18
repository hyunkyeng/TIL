# Q. 16진수 문자로 이루어진 1차 배열이 주어질 때 암호비트패턴을 찾아 차례대로 출력하시오.
# 암호는 연속되어있다.

s = input()
pattern = ['001101', '010011', '111011', '110001', '100011',
           '110111', '001011', '111101', '011001', '101111']
def mybin(i):
    t = ''
    for k in range(4):
        t = str(i%2) + t
        i//=2
    return t

b = ''
for i in s:
    if i<='9':
        b += mybin(int(i))
    else:
        b += mybin(ord(i)-55)
print(b)
ans = []
i = len(b)-1
while i>5:
    if b[i]=='1':
        t = b[i-5:i+1]
        for k in range(len(pattern)):
            if t==pattern[k]:
                ans.insert(0,k)
                i -= 5
    i -= 1
print(*ans)