def dfs(graph, visited, now):
    visited[now] = True
    for i in graph[now]:
        if not visited[i]:
            dfs(graph, visited, i)

with open('input.txt', 'r') as f:
    V, E = list(map(int, f.readline().split()))
    mas = [set() for i in range(V+1)]
    for i in range(E):
        v1, v2 = list(map(int, f.readline().split()))
        mas[v1].add(v2)
        mas[v2].add(v1)

visited = [False for i in range(V+1)]
dfs(mas, visited, 1)
res = list(filter(lambda i:visited[i], range(1,V+1)))
print(len(res))
print(*res)


