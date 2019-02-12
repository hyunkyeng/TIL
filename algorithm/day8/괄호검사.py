import sys
sys.stdin = open("괄호검사.txt")


def test(line):
    new_L = []
    for i in range(len(line)):
        if line[i] == "(":
            new_L.append(line[i])
        elif line[i] == ")":
            if len(new_L) == 0:
                return 0
            new_L.pop(-1)
    for i in range(len(line)):
        if line[i] == "{":
            new_L.append(line[i])
        elif line[i] == "}":
            if len(new_L) == 0:
                return 0
            new_L.pop(-1)

    if len(new_L) != 0:
        return 0
    else:
        return 1


T = int(input())

for tc in range(T):
    line = list((input()))
    print(f'#{tc+1} {test(line)}')

