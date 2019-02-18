import sys
sys.stdin = open("Magnetic.txt")

T = 10
for tc in range(T):
    data = int(input())
    table = [list(map(int, input().split())) for _ in range(data)]

    count = 0

    for w in range(data):
        L = []
        for j in range(data):
            if table[j][w] == 1:
                L.append(table[j][w])

            elif table[j][w] == 2:
                if len(L) != 0:
                    count += 1
                    L = []
    print(f'#{tc+1} {count}')
