
with open('input.txt', 'r') as file:
    N = int(file.readline())
    mas = [(float('inf'), float('inf'), 'M')] + [(float('inf'), float('inf'), 'M') for i in range(N)]]
    for i in range(1, N+1):
        mas = [(float('inf'), float('inf'), 'M')]
        f, s = [int(i) for i in file.readline().split()]
        for j in range(1, N+1):
            a = mas[i, j-1]
            b = mas[j, i-1]
            if max(a[0]+f, a[1]) < max(b[0], b[1]+s):
                mas.append((a[0]+f, a[1], 'F'))
            else:
                mas.append((b[0], b[1]+s, 'S'))

ans = 0
res = mas[0][N-1]
mm = max(res[0][0], res[0][1])
for j in range(N):
    i = mas[j][N-j-1]
    if max(i[0], i[1]) < mm:
        ans = j
        mm = max(i[0], i[1])

