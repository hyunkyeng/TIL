# find 구현

# 1. 고지식한 패턴 검색 알고리즘

p = "is"   #찾을 패턴
t = "This is a book"   #전체 텍스트
M = len(p)  #찾을 패턴의 길이
N = len(t)  #전체 텍스트의 길이

def BruteForce(p, t):
    i = 0   #t의 인덱스
    j = 0   #p의 인덱스
    while i < N and j < M:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i - M    #검색 성공
    else:
        return -1   #검색 실패


print(BruteForce(p, t))



# 2. 
def bruteForce2(text, pattern):
    for i in range(len(text)-len(pattern)+1):
        cnt = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            else:
                cnt += 1
        if(cnt >= len(pattern)):
            return i