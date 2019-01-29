import sys
sys.stdin = open("회문_input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    for i in range(N):   #가로 문자열 찾기.(JHYXHBQ TLMMHOOOHMMLT)
        for z in range(N-M+1):
            count = 0
            str = ""
            for j in range(M):
                if data[i][z+j] == data[i][z+M-1-j]:
                    count += 1
                    str += data[i][z+j]
                    if count == M:
                        print(f'#{tc+1} {str}')

    for j in range(N):   #세로 문자열 찾기.
        for z in range(N-M+1):
            count = 0
            str = ""
            for i in range(M):
                if data[z+i][j] == data[z+M-1-i][j]:
                    count += 1
                    str += data[z+i][j]
                    if count == M:
                        print(f'#{tc+1} {str}')

