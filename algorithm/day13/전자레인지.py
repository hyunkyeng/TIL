T = int(input())


A = 300
B = 60
C = 10

count_A, count_B, count_C = 0, 0, 0

if T % 10:
    print(-1)

else:
    if T >= A:
        while T >= A:
            T = T - A
            count_A += 1
    if B <= T < A:
        while B <= T < A:
            T = T - B
            count_B += 1
    if T < B:
        while T > 0:
            T = T - C
            count_C += 1

    print(count_A, count_B, count_C)
