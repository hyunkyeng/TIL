import sys
sys.stdin = open("ladder.txt")

T = 10
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if data[99][i] == 2:
            start = i
    for j in range(1, 100):
        if start-1 >=0 and data[99-j][start-1] == 1:
            data[99 - j][start] == 0
            start = start-1
            while start > 0 and data[99-j][start-1] == 1:
                data[99 - j][start] == 0
                start = start-1
                # print(start)
        elif start+1 <= 99 and data[99-j][start+1] == 1:
            data[99 - j][start] == 0
            start = start+1
            while start < 99 and data[99-j][start+1] == 1:
                data[99 - j][start] == 0
                start = start+1
    print(f'#{N} {start}')

