import sys

def dfs(graph, visited, now, comp):
    visited[now] = True
    comps[now] = comp
    for i in graph[now]:
        if not visited[i]:
            dfs(graph, visited, i, comp)

with open('input.txt', 'r') as f:
    V, E = list(map(int, f.readline().split()))
    sys.setrecursionlimit(100000)
    mas = [set() for i in range(V+1)]
    for i in range(E):
        v1, v2 = list(map(int, f.readline().split()))
        mas[v1].add(v2)
        mas[v2].add(v1)

comps = [0 for i in range(V+1)]
visited = [False for i in range(V+1)]
comp = 1
for i in range(1, V+1):
    # if mas[i] == set():
    #     comps[i] = comp
    #     comp += 1
    if not visited[i]:
        dfs(mas, visited, i, comp)
        comp += 1

print(comp-1)
answ = dict()
for i in range(1, V+1):
    if comps[i] not in answ:
        answ[comps[i]] = list()
    answ[comps[i]].append(i)

for j in answ:
    print(len(answ[j]))
    print(*answ[j])
