# n개 중에 n개를 중복없이 줄세우는 것


# def myprint(n):
#     for i in range(n):
#         print(" %d " % (a[i]), end="")
#     print()

# 순열 푸는 방법 암기
def perm(n, k):
    if n == k:
        print(a)
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]

a = [1, 2, 3]

perm(3, 0)