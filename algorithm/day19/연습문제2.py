# Q. 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에섭터 7bit씩 묶어 십진수를 변환하여 출력해보자

data = '0F97A3'
asc = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]


T = 2
for tc in range(1, T+1):

    data2 = []
    for i in data:
        data2.append(int(i, 16))
    nums = ''
    for i in data2:
        a =  bin(i)[2:]
        dif = 4-len(a)
        nums += '0'*dif + a
    L = []
    while len(nums) > 0:
        num = nums[:7]
        nums = nums[7:]
        L.append(num)
    for i in L:
        print(int(i, 2), end=" ")
    print()
