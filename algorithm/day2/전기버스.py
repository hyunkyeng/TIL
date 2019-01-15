import sys
sys.stdin = open("bus_input.txt")


T = int(input())
for test_case in range(T):
    K, N, M = map(int, input().split())
    bus_stop = list(map(int, input().split()))
    print(bus_stop)
    count = 0
    a = 0 + K
    i = 0
    print("a", a)
    while i < len(bus_stop):
        if a == bus_stop[i]:
            count += 1
            a += K
            i += 1
            print("count", count)
            print("a", a)
        else:
            a -= 1

    print(count)
    print()
    # print(f"#{test_case + 1} {count}")

