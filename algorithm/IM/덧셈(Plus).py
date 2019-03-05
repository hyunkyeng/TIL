# Q.0이상 9이하의 숫자로 이뤄진 문자열 S가 주어졌을 때, S 사이에 적당히 +기호를 추가 하여 주어진 정수 X에 대해 SA + SB = X 를 만족시키는 경우가 존재하는지 알아내는 프로그램을 작성하라. 여기서 SA는 추가된 +기호 앞, SB는 추가된 +기호 뒤의 문자열을 뜻한다. 예를 들어 S = "1245", X = 57일 경우 2와 4 사이에 +기호를 추가시켜 12+45=57을 만들 수 있다.

def Plus(num, N):
    i = 1
    while i < num:
        q = num // (10 * i)
        r = num % (10 * i)
        if q + r == N:
            return "{}+{}={}".format(q, r, N)
        i = i * 10
    return 'NONE'


import sys
sys.stdin = open("덧셈(Plus).txt")

num, N = map(int, input().split())

print(Plus(num, N))
