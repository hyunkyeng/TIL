import sys
sys.stdin = open("orchard.txt")

N = int(input())
L = []
for i in range(N):
    L.append(list(map(int, input())))

print(L)