def enQ(n):
    global last
    last += 1   #마지막 노드번호 증가
    c = last    #마지막 노드를 자식노드로
    p = c//2    #부모 노드 번호 계산
    Q[last] = n #마지막 노드에 값 저장
    while c > 1 and Q[p] > Q[c]:    #루트가 아니고, 부모 노드의 값이 더 크면
        t = Q[p]    #저장된 값 바꿈
        Q[p] = Q[c]
        Q[c] = t
        c = p   #부모를 새로운 자식노드로
        p = p//2

def deQ():
    global last
    r = Q[1]    #리턴값(루트노드)
    Q[1] = Q[last]  #마지막을 루트노드로 이동
    last -= 1   #카운터 감소
    p = 1
    while p < last:
        c1 = p * 2  #왼쪽자식
        c2 = p * 2 + 1  #오른쪽자식
        if c2 <= last:  #양쪽자식이 다 있는 경우
            if Q[c1] < Q[c2]:
                c = c1
            else:
                c = c2
            if Q[c] < Q[p]:
                Q[c], Q[p] = Q[p], Q[c]
                p = c
            else:
                break
        elif c1 <= last:    #왼쪽자식만 있는 경우
            if Q[c1] < Q[p]:
                Q[c1], Q[p] = Q[p], Q[c1]
                p = c1
            else:
                break
    return r