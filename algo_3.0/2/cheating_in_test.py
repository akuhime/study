global flag
flag = 1
def dfs(graph, visited, now, color):
    global flag
    if not flag:
        return
    visited[now] = True
    colors[now] = color
    for i in graph[now]:
        if visited[i]:
            if colors[i] == color:
                flag = 0
                return
        else:
            dfs(graph, visited, i, 3-color)

with open('input.txt', 'r') as f:
    V, E = list(map(int, f.readline().split()))
    mas = [set() for i in range(V+1)]
    for i in range(E):
        v1, v2 = list(map(int, f.readline().split()))
        mas[v1].add(v2)
        mas[v2].add(v1)

colors = [0 for i in range(V+1)]
visited = [False for i in range(V+1)]
for i in range(1, V+1):
    if not visited[i]:
        dfs(mas, visited, i, 1)

print('YES' if flag else 'NO')

