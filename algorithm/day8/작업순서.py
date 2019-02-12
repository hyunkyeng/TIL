import sys
sys.stdin = open("작업순서.txt")

def dfs(n):
    global G, visited, V
    visited[n] = 1

    print(n, end=" ")

    for w in range(V):
        if G[n][w] == 1 and visited[w] == 0:
            dfs(w)

def order(n):
    global data, new_L
    result.append(n)
    data.pop(start)
    data.pop(data[start+1])
    new_L = []
    print(data)

    for i in range(0, len(data), 2):
        new_L.append(data[i+1])

    print(new_L)
    for i in range(0, len(data), 2):
        if data[i] not in new_L:
            order(data[i])



T = 10
for tc in range(1):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    print(data)
    V += 1
    new_L = []
    start_point = []
    result = []
    G = [[0 for _ in range(len(data))] for _ in range(len(data))]
    visited = [0 for _ in range(len(data))]


    for i in range(0, len(data), 2):
        G[data[i]][data[i+1]] = 1
        new_L.append(data[i+1])

    for i in range(0, len(data), 2):
        if data[i] not in new_L:
            start= i
            break

    order(data[start])
    print(result)

    # print(f'#{tc+1}', end = " ")
    #
    # dfs(start_point[0])
    # print()
