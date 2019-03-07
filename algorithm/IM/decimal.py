import sys
sys.stdin = open("decimal.txt")

a, b = map(int, input().split())
L = []
cnt = 0
min = 100000

for i in range(b-a+1):
    L.append(a+i)

for idx in range(len(L)):
    for i in range(2, L[idx]):
        if L[idx] % i == 0:
            L[idx] = 0

for num in L:
    if num > 0:
        cnt += 1
        if num < min:
            min = num

print(cnt)
print(min + max(L))
