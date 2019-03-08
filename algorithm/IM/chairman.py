def sum(L):
    sum = 0
    for i in L:
        sum += i
    return sum




import sys
sys.stdin = open("chairman.txt")

N = int(input())
score_a = []
score_b = []
score_c = []
for i in range(N):
    a, b, c = map(int, input().split())
    score_a.append(a)
    score_b.append(b)
    score_c.append(c)
