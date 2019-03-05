import sys
sys.stdin = open("줄세우기.txt")

N = int(input())
num = list(map(int, input().split()))
L = []

for i in range(len(num)):
    if num[i] == 0:
        L.append(i+1)
    else:
        L.append(i+1)
        for j in range(num[i]):
            L.append(L.pop(-(num[i]+1)))
for k in L:
    print(k, end=" ")