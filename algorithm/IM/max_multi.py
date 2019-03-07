N = int(input())
L = []
max = 0

for i in range(N):
    L.append(float(input()))
for j in range(N):
    multi = 1
    for i in range(N - j):
        multi = multi * L[j + i]
        if multi > max:
            max = multi
print("{:.3f}".format(max))