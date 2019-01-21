# 이진탐색 - 정렬이 되어있을 때 이 방법 사용 가능

def binarySearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if key == a[middle]:
            return middle
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1   #검색실패

key = 19
data = [2, 4, 7, 9, 11, 19, 23]
print(binarySearch(data, key))