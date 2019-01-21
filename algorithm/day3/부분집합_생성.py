# 부분집합생성 - 방법1

# bit = [0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             print(bit)
#

# 부분집합생성 - 방법2

arr = [1, 2, 3]
n = len(arr)

for i in range(1 << n):  # 1 << n : 2**n
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=",")
    print()