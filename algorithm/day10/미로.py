import sys
sys.stdin = open("미로.txt")

def search(start, y):
    global M, flag

    for i in range(0, 4):
        nx = start + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < r:
            if M[ny][nx] == 2:
                flag = 1
            if M[ny][nx] == 0:
                M[ny][nx] = 9
                search(nx, ny)
    return flag

T = int(input())
for tc in range(T):
    r = int(input())
    M = [list(map(int, input())) for _ in range(r)]
    flag = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for y in range(r):
        for x in range(r):
            if M[y][x] == 3:
                start_x = x
                start_y = y

    print(f'#{tc+1} {search(start_x, start_y)}')