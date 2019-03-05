def NodeSum():
    global Q
    for i in range(len(Q)-1, 0, -1):
        if Q[i] == 0:
            if 2*i <= N:
                Q[i] = Q[2*i]
                if 2*i+1 <= N:
                    Q[i] = Q[2*i] + Q[2*i +1]
    return Q



import sys
sys.stdin = open("노드의합.txt")

T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    Q = [0] * (N+1)
    for i in range(M):
        a, b = map(int, input().split())
        Q[a] = b

    result_Q = NodeSum()
    print("#{} {}".format(tc+1, result_Q[L]))