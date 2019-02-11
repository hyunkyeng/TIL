# Q. 연습문제3
# 다음은 연결되어 있는 두 개의 점정 사이의 간산을 순서대로 나열 해 놓은 것인다.
# 모든 정점을 깊이 우선 탐색하여 화면에 깊이우선탐색 경로를 출력하시오.
# 시작 정점을 1로 시작하시오.

import sys
sys.stdin = open("연습3_input.txt")

n, edge = map(int, input().split())
n += 1
temp = list(map(int, input().split()))

G = [[0 for i in range(n)] for j in range(n)] #2차원 초기화
visited = [0 for i in range(n)] #방문처리

for i in range(0, len(temp), 2): #입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i + 1]][temp[i]] = 1

for i in range(n):
    print(f"{i} {G[i]}")

# 위에까지가 2차원 행렬만들기
# 이제부터는 1-2-4-6-5-7-3 이렇게 찾기

def dfs(v):
    global G, visited, n
    visited[v] = 1
    print(v, end=" ")

    for w in range(n):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)


dfs(1)


