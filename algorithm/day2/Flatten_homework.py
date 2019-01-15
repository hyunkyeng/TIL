import sys
sys.stdin = open("Flatten_input.txt")

T = 10
for tc in range(T):
    dump_number = int(input())
    h = list(map(int, input().split()))

    for dm in range(dump_number):
        max_h = 0
        min_h = 101
        for i in range(len(h)):
            if max_h < h[i]:
                max_h = h[i]
                index_max = i
                # print("max", max_h)
            if min_h > h[i]:
                min_h = h[i]
                index_min = i
                # print("min", min_h)
            # if max_h == min_h:
            #     break
        # print("{} {}".format(h[index_max], h[index_min]), end=" ")
        # print()
        # print(h[index_min])
        h[index_max] -= 1
        h[index_min] += 1
# 덤프 단계 다 하고 나서 남은 것에서 다시 max 와 min 을 구해야 한다. 덤프마지막단계가 끝나면 다시 max 와 min 이 바뀌므로
    max_hh = 0
    min_hh = 101
    for i in range(len(h)):
        if max_hh < h[i]:
            max_hh = h[i]
            # print("max", max_h)
        if min_hh > h[i]:
            min_hh = h[i]
    print(f"#{tc+1} {max_hh - min_hh}")
