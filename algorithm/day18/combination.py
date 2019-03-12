# 조합 결과 프린트하기
def combination(n, r, q):
    if r == 0:
        myprint(q)
    elif n < r:
        return
    else:
        T[r-1] = A[n-1]
        combination(n-1, r-1, q)
        combination(n-1, r, q)


def myprint(q):
    while q != 0:
        q = q - 1
        print(" %d " % (T[q]), end="")

A = [1, 2, 3, 4]
T = [0] * 3

combination(4, 3, 3)


# # 조합의 개수 구하기
#
# def combination(n, r, q):
#     if r == 0:
#         return 1
#     elif n < r:
#         return 0
#     else:
#         return combination(n-1, r-1, q) + combination(n-1, r, q)
#
# A = [1, 2, 3, 4]
# T = [0] * 3
#
# print(combination(4, 3, 3))