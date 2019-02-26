def back(M):
    global nums
    for i in range(M):
        nums.append(nums[0])
        nums.pop(0)
    return nums
    


import sys
sys.stdin = open("회전.txt")

T = int(input())
for tc in range(T):
    N, M = (map(int, input().split()))
    nums = list(map(int, input().split()))


    result_num = back(M)
    print(f'#{tc+1} {result_num[0]}')