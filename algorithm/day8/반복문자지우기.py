import sys
sys.stdin = open("반복문자지우기.txt")

def delete(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s.pop(i)
            s.pop(i)
            return delete(s)
            delete(s)


T = int(input())
for tc in range(T):
    s = list(input())

    delete(s)
    print(f'#{tc+1} {len(s)}')
