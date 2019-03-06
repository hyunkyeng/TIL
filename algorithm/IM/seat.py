import sys
sys.stdin = open("seat.txt")

x, y = map(int, input().split())
K = int(input())

L = [[0 for _ in range(x)] for _ in range(y)]
print(L)

