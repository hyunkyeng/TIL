import sys
sys.stdin = open("seat.txt")

def find(startx, starty):
    global countx, county, num
    while K <= X*Y:
        # 오른쪽이동
        for x in range(countx):
            startx = startx + 1
            num += 1
            L[starty][startx] = num
            if num == K:
                return starty, startx
        # 아래이동
        county = county-1
        for y in range(county):
            starty = starty + 1
            num += 1
            L[starty][startx] = num
            if num == K:
                return starty, startx
        # 왼쪽이동
        countx = countx-1
        for x in range(countx):
            startx -= 1
            num += 1
            L[starty][startx] = num
            if num == K:
                return starty, startx
        # 위로이동
        county = county -1
        for y in range(county):
            starty = starty - 1
            num += 1
            L[starty][startx] = num
            if num == K:
                return starty, startx
        countx = countx - 1

    return 0


Y, X = map(int, input().split())
county, countx = Y, X
K = int(input())

L = [[0 for _ in range(X+1)] for _ in range(Y+1)]

startx, starty = 0, 1
num = 0

answer = find(startx, starty)

if answer:
    print(*answer)
else:
    print(0)


