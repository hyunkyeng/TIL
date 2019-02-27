T = int(input())

A = 300
B = 60
C = 10

count_A, count_B, count_C = 0, 0, 0

if T % 10:
    print(-1)

else:
    count_A = T // A
    T = T % A
    count_B = T // B
    T = T % B
    count_C = T // C

    print(count_A, count_B, count_C)