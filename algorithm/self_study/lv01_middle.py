# Q. 중간값 찾기

import sys
sys.stdin = open("lv01_middle.txt")

N = int(input())
L = list(map(int, input().split()))

L.sort()
n = N//2
print(L[n])