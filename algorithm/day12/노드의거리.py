def bfs(s):
    global G, visited
    queue = []
    queue.append(s)
    visited[s] = 1

    while len(queue) != 0:
        t = queue.pop(0)
        for w in range(1, V+1):
            if G[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1
    return visited



import sys
sys.stdin = open("노드의거리.txt")

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(E)]
    S, end = map(int, input().split())

    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for i in range(0, len(temp)):
        G[temp[i][0]][temp[i][1]] = 1
        G[temp[i][1]][temp[i][0]] = 1


    result_visited = bfs(S)
    if result_visited[end] > 0:
        print(f'#{tc+1} {result_visited[end]-1}')
    else:
        print(f'#{tc + 1} 0')