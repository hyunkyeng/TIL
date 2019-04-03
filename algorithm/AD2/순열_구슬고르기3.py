
a = [1, 2, 3]   # 구슬
b = [0, 0, 0]   # 구슬을 담을 상자
chk = [0, 0, 0] # 구슬 사용여부 체크
N = 3

def DFS(n):     # 현재 n번째 상자에 모든 구슬을 순열구조로 담아보는 모든 경우
    if n >= N:   # N을 2로 바꾸면 3개중의 2개를 고른 조합이 된다. 
        for i in range(N):
            print(b[i], end=' ')
        print()
        return
    for i in range(N):  # a[i] a 배열의 구슬 (단, 구슬 중복배제)
        if chk[i]:      # 사용한 구슬이면 스킵 (이부분을 제외하면 중복순열)
            continue
        chk[i] = 1      # 구슬 사용체크
        b[n]=a[i]       # 구슬 기록
        DFS(n+1)        # 다음 상자 시도
        chk[i] = 0      # 구슬 사용해제

DFS(0)  # b[0]요소부터 담기시작 ( n : 인덱스 )