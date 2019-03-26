import sys
sys.stdin = open('최대상금.txt')

T = int(input())
for tc in range(1):
    price, N = map(str, input().split())
    N = int(N)
    
