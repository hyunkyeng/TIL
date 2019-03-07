import sys
sys.stdin = open("class.txt")


def division(min_score, max_score):
    global result
    for T1 in range(min_score + 1, max_score):  # 첫번째 기준점수 설정
        for T2 in range(T1+1, max_score + 1):  # 두번째 기준점수 설정
            A = []
            B = []
            C = []
            for k in range(len(score_L)):
                if score_L[k] < T1:
                    A.append(score_L[k])
                elif T1 <= score_L[k] < T2:
                    B.append(score_L[k])
                elif T2 <= score_L[k]:
                    C.append(score_L[k])
            if Kmin <= len(A) <= Kmax and Kmin <= len(B) <= Kmax and Kmin <= len(C) <= Kmax:
                if result > max(len(A), len(B), len(C)) - min(len(A), len(B), len(C)):
                    result = max(len(A), len(B), len(C)) - min(len(A), len(B), len(C))


    if result != 100000:
        return result
    else:
        return -1

T = int(input())
for tc in range(T):
    N, Kmin, Kmax = map(int, input().split()) #N:신입사원수, Kmin:반의최소인원, Kmax:반최대인원
    score_L = list(map(int, input().split()))
    score_L.sort()


    min_score = min(score_L)
    max_score = max(score_L)
    result = 100000

    print(division(min_score, max_score))


