import sys
sys.stdin = open("단지번호붙이기.txt")

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

print(arr)

