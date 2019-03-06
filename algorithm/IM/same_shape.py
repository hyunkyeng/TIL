import sys
sys.stdin = open("")

M = int(input())
Marr = []
for i in range(M):
    Marr.append(list(map(int, input())))

P = int(input())
Parr = []
for i in range(P):
    Parr.append(list(map(int, input())))
sol = 0

#원본패턴
for i in range(M-P+1):
    for j in range(M-P+1):
        cnt = 0
        for k in range(P):
            for l in range(P):
                if Marr[i+k][j+l] ==Parr[k][l]:
                    cnt += 1
        if cnt == P*P:
            sol += 1

#90도로 회전한 패턴
Parr90 = [[0]*P for _ in range(P)]
for i in range(P):
    for j in range(P):
        Parr90[j][P-i-1] = Parr[i][j]

        #원본패턴에서 비교하는것 복붙!
for i in range(M-P+1):
    for j in range(M-P+1):
        cnt = 0
        for k in range(P):
            for l in range(P):
                if Marr[i+k][j+l] ==Parr90[k][l]:
                    cnt += 1
        if cnt == P*P:
            sol += 1


#180도로 회전한 패턴(90도로 회전한 패턴을 다시 90도로 회전한다)