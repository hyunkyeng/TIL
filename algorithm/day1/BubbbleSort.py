# 오름차순 정렬  = data.sort() / 역순 = data.reverse()
def bubbleSort(data):
    for i in range(len(data)-1, 0, -1):  # 4, 3, 2, 1
        for j in range(0, i):   #4, 3, 2, 1
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]


data = [55, 7, 78, 12, 42]
bubbleSort(data)
print(data)


