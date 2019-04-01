import sys
sys.stdin = open("최소이동거리.txt")

T = int(input())
for tc in range(1):
    N, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]