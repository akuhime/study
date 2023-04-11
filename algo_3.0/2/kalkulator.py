N = int(input())
seq = [(0, 0) for i in range(N+1)]
for i in range(2, N+1):
    vars = []
    vars.append((seq[i-1][0]+1, i-1))
    if i % 3 == 0:
        vars.append((seq[i//3][0]+1, i//3))
    if i % 2 == 0:
        vars.append((seq[i//2][0]+1, i//2))
    vars.sort(key=lambda x:x[0])
    seq[i] = vars[0]

res = [N]
k = N
while k != 1:
    id = seq[k][1]
    res.append(id)
    k = id

print(seq[N][0])
print(*reversed(res))