def bfs():
    1. 시작점을 큐에 저장(방문표시)
    while Que:  # 큐가 있을 동안 반복
        2. 큐에서 데이타를 읽기(현재좌표)
        3. 사방탐색하면서 연결점(길)을 찾아 큐에 저장
            3-1. 맵 범위 체크
            3-2. 연결점을 큐에 저장(방문 표시)
        4. 큐가 빈 상태