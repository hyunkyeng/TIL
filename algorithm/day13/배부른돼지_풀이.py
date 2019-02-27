import sys
sys.stdin = open("배부른돼지.txt")

T = int(input())

N_list = []
Y_list = []
if T == 0:
    print('F')
else:
    for tc in range(T):
        x, y = input().split()
        if y == "Y":
            Y_list.append(x)
        elif y == "N":
            N_list.append(x)

    if max(N_list) < min(Y_list):
        print(min(Y_list))
    else:
        print('F')
