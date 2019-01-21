# Q. 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서
#   그 집합의 원소를 모두 더한 값이 0 이 되는 경우가 있는지 알아내는 문제
#   예를 들어, [-7, -3, -2, 5, 8]라는 집합이 있을 때, [-3, -2, 5]라는
#   이 집합의 부분집합이면서 (-3)+(-2)+5=0이므로 답은 참이 된다.

arr = [-7, -3, -2, 5, 8]
n = len(arr)
count = 0

sum = 0
for i in range(1, 1 << n):
    sum = 0
    for j in range(n):
        if i & (1 << j):
            sum += arr[j]
    if sum == 0:
        count += 1
        for j in range(n):
            if i & (1 << j):
                print(arr[j], end=" ")
        print()
print(f"개수: {count}")