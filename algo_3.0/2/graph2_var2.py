with open('input.txt', 'r') as f:
    V, E = list(map(int, f.readline().split()))
    mas = [set([i]) for i in range(V+1)]
    for i in range(E):
        v1, v2 = list(map(int, f.readline().split()))
        mas[v1].add(v2)
        mas[v2].add(v1)

prev = 0
step = 1
while prev != step:
    comps = [mas[1]]
    for s in mas[2:]:
        for i in range(len(comps)):
            if comps[i].intersection(s) != set():
                comps[i] = comps[i].union(s)
                break
        else:
            comps.append(s)
    prev = step
    step = len(comps)
    mas = [set()] + comps


print(len(comps))
for j in range(1, len(comps)+1):
    print(len(comps[j-1]))
    print(*comps[j-1])
