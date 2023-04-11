with open('input.txt', 'r') as f:
    N = int(f.readline())
    seq = []
    for i in range(N):
        seq.append(int(f.readline()))

mas = [[0 for i in range(N+1)] for j in range(N+1)]
mas2 = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(1, N+1):
    mas[0][i] = float('inf')

# первый индекс строка

for i in range(1, N+1):
    for j in range(N+1):
        if seq[i-1] > 100:
            if j == 0:
                mas[i][j] = mas[i-1][j+1]
                mas2[i][j] = 1
            elif j == N:
                mas[i][j] = (mas[i-1][j-1]+seq[i-1])
                mas2[i][j] = -1
            else:
                if (mas[i-1][j-1]+seq[i-1]) <= mas[i-1][j+1]:
                    mas[i][j] = (mas[i-1][j-1]+seq[i-1]) 
                    mas2[i][j] = -1
                else:
                    mas[i][j] = mas[i-1][j+1]
                    mas2[i][j] = 1
        else:
            if j == N:
                mas[i][j] = (mas[i-1][j]+seq[i-1])
                mas2[i][j] = -1
            else:
                if (mas[i-1][j]+seq[i-1]) <= mas[i-1][j+1]:
                    mas[i][j] = (mas[i-1][j]+seq[i-1]) 
                else:
                    mas[i][j] = mas[i-1][j+1]
                    mas2[i][j] = 1



sum_ = float('inf')
K1 = -1
for i in range(N+1):
    if mas[N][i] <= sum_:
        sum_ = mas[N][i]
        K1 = i

x = K1
K2 = 0
res = []
for y in range(N, 0, -1):
    if mas2[y][x] == 1:
        K2 += 1
        res.append(y)
    x += mas2[y][x]

print(sum_)
print(K1, K2)
print(*reversed(res))
