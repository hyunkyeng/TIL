# Q. 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
#    25개의 요소에 대해서 모두 조사하여 총합을 구하시오.

# arr = [[1, 1, 1, 1, 1],
#        [1, 0, 0, 0, 1],
#        [1, 0, 0, 0, 1],
#        [1, 0, 0, 0, 1],
#        [1, 1, 1, 1, 1]]

'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''

def isWall(x, y):
    if x < 0 or x >=5:
        return True
    if y < 0 or y >= 5:
        return True
    return False

def calAbs(y, x):
    if y-x > 0:
        return y-x
    return x-y

arr = [[0 for a in range(5)] for b in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))
# print(arr)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX, testY) == False:
                sum += calAbs(arr[y][x], arr[testY][testX])

print(f"sum = {sum}")





