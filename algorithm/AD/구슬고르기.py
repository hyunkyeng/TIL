a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
chk = [0, 0, 0] # 구슬 사용여부 체크
N = 3

def DFS(no): #현재 no번째 상자에 모든 구슬을 순열구조로 담아보는 모든 경우
    #1] 리턴조건 : 3개를 고른후 인쇄한 후 리턴
    if no >= N:
        for i in range(N):
            print(b[i], end = " ")
        print()
        return
    #2] a배열에서 0요소부터 N전요소전까지 고르는 모든 경우(단 구슬중복 배제)
    for i in range(N):  # a 배열의 구슬(단, 구슬의 중복 배제)
        if chk[i]: continue
        chk[i] = 1  # 눈사용 체크
        b[no] = a[i]    # 구슬 기록
        DFS(no + 1)
        chk[i] = 0  # 눈 사용체크 해제

# main ============================
DFS(0) # b[0]요소부터 담기 시작