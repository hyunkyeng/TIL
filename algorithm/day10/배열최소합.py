import sys
sys.stdin = open("배열최소합.txt")

def process_solution(a, k):
    for i in range(1, k+1):
        stack.append(data[a[i]])



def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)

T = int(input())
for tc in range(T):
    r = int(input())
    M = [list(map(int, input().split())) for _ in range(r)]
    data = list(range(r+1))
    stack= []
    sum_L = []
    sum = 0

    MAXCANDIDATES = 100
    NMAX = 100

    a = [0] * NMAX
    backtrack(a, 0, r)
    # print(stack)

    for i in range(0, len(stack), r):
        for j in range(r):
            # print(M[j][stack[i][j]-1])
            sum += M[j][stack[i+j]-1]
        sum_L.append(sum)
        sum = 0
    print(f'#{tc+1} {min(sum_L)}')
