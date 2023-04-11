with open('input.txt', 'r') as f:
    N, M = list(map(int, f.readline().split()))
    mas = [[0, 0] + [0 for i in range(M-1)]]
    for i in range(N):
        mas.append([0] + list(map(int, f.readline().split())))

mas2 = [['S' for i in range(M+1)] for j in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if mas[i][j-1] > mas[i-1][j]:
            mas[i][j] += mas[i][j-1]
            mas2[i][j] = 'R'
        else:
            mas[i][j] += mas[i-1][j]
            mas2[i][j] = 'D'

print(mas[N][M])
res = []
x = M
y = N
for i in range(N+M-2):
    res.append(mas2[y][x])
    if mas2[y][x] == 'D':
        y -= 1
    else:
        x -= 1

print(*reversed(res))