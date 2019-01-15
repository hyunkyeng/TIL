import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    max_data = 0
    min_data = 1000000
    for i in range(len(data)):
        if max_data < data[i]:
            max_data = data[i]
    for i in range(len(data)):
        if min_data > data[i]:
            min_data = data[i]
    result = max_data - min_data

    print("#{} {}".format(test_case, result))