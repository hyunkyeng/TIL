import sys   #제출할 때는 주석처리
sys.stdin = open("view_input.txt")
T = 10
for tc in range(T):
    ans = 0
    N = int(input())    #테스트 케이스의 길이를 받는 것.
    data = list(map(int, input().split()))  #테스트 케이스를 받는 것.
    # print(data)
    for i in range(2, len(data)-2):
        if data[i] > max(data[i - 2], data[i - 1], data[i + 1], data[i + 2]):
            ans += data[i] - max(data[i-2], data[i-1], data[i+1], data[i+2])

    print("#{} {}".format(tc+1, ans))