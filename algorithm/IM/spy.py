import sys
sys.stdin = open("spy.txt")

N, L = map(str, input().split())
N = int(N)
print(L)

G = [[0 for _ in range(10)] for _ in range(10)]

for i in range(len(L)):
    if L[i] != "<" and L[i] != ">":
        if L[i+1] == "<":
            if L[i+2] != "<" and L[i+2] != ">":
                G[L[i]][L[i+2]] == 1
    if L[i] =="<" and L[i+1] == ">":



