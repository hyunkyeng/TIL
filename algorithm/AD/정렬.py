

# 1. 버블 정렬 (오름차순 정렬) - 시간복잡도 n^2

for i in range(N-1):
    for j in range(i+1, N):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

# 2. 퀵 정렬 - 시간복잡도 nlogn
#   - pivot : 기준 / left : 비교대상 / target : 교환대상
#   - 비교는 pivot과 left / 교환은 left 와 target

def Qsort(start, end):
    if start >= end:
        return
    p, t = end, start
    for L in range(start, end):
        if a[L] < a[p]:
            a[L], a[t] = a[t], a[L]
            t += 1
    a[p], a[t] = a[t], a[p]
    Qsort(start, t-1) # 왼쪽영역을 다시 콜한다
    Qsort(t+1, end) # 오른쪽영역을 다시 콜한다

# 3. 머지 정렬


arr = [4, 3, 2, 1]
temp = [0] * len(arr)

def mergesort(s, e):
    if s >= e: return         # 원소 하나 단위로 쪼갰으면 리턴
    m = (s + e)//2
    mergesort(s, m)           # 왼쪽 쪼개기
    mergesort(m+1, e)         # 오른쪽 쪼개기
    L, R, T = s, m+1, s
    while L <= m and R <= e:
        if arr[L] < arr[R]:   # 왼쪽 영역이 작으면 왼쪽 영역 값을 임시 버퍼로
            temp[T] = arr[L]
            T += 1
            L += 1
        else:                 # 아니면 오른쪽 값을 임시 버퍼로
            temp[T] = arr[R]
            T += 1
            R += 1
    while L <= m:             # L쪽이 남은경우 그대로 버퍼에 넣기
        temp[T] = arr[L]
        T += 1
        L += 1
    while R <= e:             # R쪽이 남은경우 그대로 버퍼에 넣기
        temp[T] = arr[R]
        T += 1
        R += 1
    for i in range(s, e+1):   # 원본에 복사하기
        arr[i] = temp[i]

mergesort(0, len(arr)-1)
print(arr)



















