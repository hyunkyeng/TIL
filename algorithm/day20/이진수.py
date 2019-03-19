import sys
sys.stdin = open("이진수.txt")

asc = [[0, 0, 0, 0],  #0
       [0, 0, 0, 1],  #1
       [0, 0, 1, 0],  #2
       [0, 0, 1, 1],  #3
       [0, 1, 0, 0],  #4
       [0, 1, 0, 1],  #5
       [0, 1, 1, 0],  #6
       [0, 1, 1, 1],  #7
       [1, 0, 0, 0],  #8
       [1, 0, 0, 1],  #9
       [1, 0, 1, 0],  #A
       [1, 0, 1, 1],  #B
       [1, 1, 0, 0],  #C
       [1, 1, 0, 1],  #D
       [1, 1, 1, 0],  #E
       [1, 1, 1, 1]]  #F

def ten(c):
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def two(x):
    for i in range(4):
        L.append(asc[x][i])


T = int(input())
L = []

for tc in range(T):
    N, arr = map(str, input().split())
    N = int(N)

    for i in range(N):
        two(ten(arr[i]))


    print('#{}'.format(tc+1), end=" ")
    for j in range(len(L)):
        print('{}'.format(int(L[j])), end="")
    print()
    L = []
