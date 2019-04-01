import sys
sys.stdin = open("최소비용.txt")



T = int(input())
for tc in range(1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)
