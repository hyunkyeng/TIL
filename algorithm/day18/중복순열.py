def Perm(n, r, q):
    if r == 0:
        myprint(q)
    else:
        for i in range(n-1, -1, -1):
            a[i], a[n-1] = a[n-1], a[i]
            t[r-1] = a[n-1]
            Perm(n-1, r-1, q)
            a[i], a[n - 1] = a[n - 1], a[i]

def myprint(q):
    while q != 0:
        q = q - 1
        print(" %d " % (t[q]), end="")
    print()

a = [1, 2, 3]
t = [0] * 3
Perm(3, 2, 2)