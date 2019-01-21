# 순차탐색 - 정렬되어 있지 않은 경우

def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i = i + 1

    if i < n:
        return i
    else:
        return -1

data = [4, 9, 11, 23, 2, 19, 7]
key = 19
print(sequentialSearch(data, len(data), key))