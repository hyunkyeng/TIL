# 구슬 고르기 1- 1

a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
N = 3

def DFS(n, start):
# 1] 리턴조건 : N번째이면 리턴
    for i in range(N): print(b[i], end= " ")
    print()
    if n >= N or start >= N:
        return
    for i in range(start, N):   # a[i]
        b[n] = a[i]
        DFS(n + 1, i + 1)
        b[n] = 0

# main  ############################################################
DFS(0, 0)  # b[0] 담기 시작, a[0]구슬부터 시작