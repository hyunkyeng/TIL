import sys
sys.stdin = open("회문2_input.txt")


for tc in range(10):
    Q = int(input())
    N = 100
    data = [input() for _ in range(100)]
    dict_str = {}

    for i in range(N):  #가로 문자열 찾기.
        for M in range(100):
            for z in range(N-M+1):
                count = 0
                str = ""
                for j in range(M):
                    if data[i][z+j] == data[i][z+M-1-j]:
                        count += 1
                        str += data[i][z+j]
                        if count == M:
                            dict_str.update({M:str})



    for j in range(N):   #세로 문자열 찾기.
        for M in range(100):
            for z in range(N-M+1):
                count = 0
                str = ""
                for i in range(M):
                    if data[z+i][j] == data[z+M-1-i][j]:
                        count += 1
                        str += data[z+i][j]
                        if count == M:
                            dict_str.update({M: str})

    print(f'#{Q} {max(dict_str)}')
