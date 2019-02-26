def pizza():
    global cheeze
    pan = []
    for i in range(N):
        pan.append(cheeze.pop(0))

    return bake(pan)

def bake(pan):
    while True:
        if len(pan) == 1:
            return pan[0][0]
        pan[0][1] = pan[0][1] // 2
        if pan[0][1] != 0:
            pan.append(pan.pop(0))
        elif pan[0][1] == 0:
            if len(cheeze) != 0:
                pan.append(cheeze.pop(0))
                pan.pop(0)

            else:
                pan.pop(0)



import sys
sys.stdin = open("피자굽기.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    cheeze = []
    for i, name in enumerate(list(map(int, input().split()))):
        cheeze.append([i + 1, name])
    # for i, name in enumerate(temp):



    print(f'#{tc+1} {pizza()}')


