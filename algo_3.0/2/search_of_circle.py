
global star
global founded
star = 0
founded = 0
res = []

def dfs(graph, visited, now, anc):
    global flag
    global star
    global founded
    if founded:
        if now in res:
            star = 0
        if star!= 0 :
            res.append(now)
        return
    visited[now] = 1
    for i in graph[now]:
        if i!=anc and visited[i] == 1 and not founded:
            star = i
            founded = 1
            res.append(i)
            return
        if visited[i]==0:
            dfs(graph, visited, i, now)        
    visited[now] = 2

with open('input.txt', 'r') as f:
    V = int(f.readline())
    mas = [set()]
    for i in range(V):
        s  = list(map(int, f.readline().split()))
        mas.append(set(filter(lambda x: s[x-1], range(1, V+1))))

visited = [0 for i in range(V+1)]
for i in range(1, V+1):
    dfs(mas, visited, i, i)

print('YES' if founded else 'NO')
if founded:
    print(len(res))
    print(*res)