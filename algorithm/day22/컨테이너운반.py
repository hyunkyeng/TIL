import sys
sys.stdin = open("컨테이너운반.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())    # N : 컨테이너 수, M : 트럭 수
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    result = 0

    # print(w)
    # print(t)

    for i in range(len(w)):
        if w[i] > max(t):
            w[i] = 0
        for k in range(len(t)):
            if w[i] == t[k]:
                t[k] = 0
                result += w[i]
                w[i] = 0
                break
        if w[i] != 0:
            for j in range(len(t)):
                if t[j] >= w[i]:
                    t[j] =0
                    result += w[i]
                    w[i] = 0
                    break
    print('#{} {}'.format(tc+1, result))

