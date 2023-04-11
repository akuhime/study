with open('input.txt', 'r') as f:
    V, E = list(map(int, f.readline().split()))
    c = 0
    res = dict()
    for i in range(E):
        v1, v2 = list(map(int, f.readline().split()))
        if v1 in res:
            if v2 not in res:
                res[v2] = res[v1]
            else:
                if res[v1]!=res[v2]:
                    a = res[v2]
                    for i in res:
                        if res[i] == a:
                            res[i] = res[v1]
        else:
            if v2 in res:
                res[v1] = res[v2]
            else:
                c += 1
                res[v2] = c
                res[v1] = c

for i in range(1, V+1):
    if i not in res:
        c+=1
        res[i] = c

print(len(set(res.values())))
for i in set(res.values()):
    l = list(filter(lambda x: res[x]==i, res.keys()))
    print(len(l))
    print(*l)

            

