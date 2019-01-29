import sys
sys.stdin = open("글자수_input.txt")

T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    max = 0
    c = [0]*len(str1)
    for i in range(len(str1)):  #str1에 있는애가 str2에 있으면 c의 그인덱스에 1을 추가한다.
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                c[i] += 1

    for k in range(len(str1)):
        if max < c[k]:
            max = c[k]
    print(f'#{tc+1} {max}')