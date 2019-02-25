def bfs(s):
    visited = [0 for _ in range(V + 1)]
    queue = []
    result = []
    count = 0

    queue.append(s)

    while queue:
        t = queue.pop(0)
        count += 1
        if not visited[t]:
            visited[t] = 1
            result.append(t)

        for j in range(V + 1):
            if G[t][j] == 1 and visited[j] == 0:
                queue.append(j)
                result.append(j)
                visited[j] += count
    print(visited)
    print(f'마지막 정점 : {result[-1]}, 그 길이 : {max(visited)-1}')
    return result