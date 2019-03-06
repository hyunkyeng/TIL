def find(Barr):
    for i in range(5):
        for j in range(5):
            a = Carr[i][j]
            for i in range(5):
                for j in range(%):
                    if Barr[i][j] == a:
                        Barr[i][j] = 0

def Bingo():
    for i in range(5):
        for j in range(5):
            if Barr[i][j] == 0:
                count += 1







import sys
sys.stdin = open("bingo.txt")

Barr = []   #빙고배열
for i in range(5):
    Barr.append(list(map(int, input().split())))
Carr = []
for i in range(5):
    Carr.append(list(map(int, input().split())))

print(Barr)
print(Carr)

for i in range(5):
    for j in range(5):
        find(Carr[i][j])    #해당 숫자를 찾아 지우기
        if Bingo() ==True:  #3줄의 빙고를 찾으면 탈출
            break
print(i*5 +j + 1)   #사회자사 부른 횟수