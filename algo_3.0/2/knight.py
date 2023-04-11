with open('input.txt', 'r') as f:
    N,M = list(map(int, f.readline().split()))

mas = [[0 for i in range(M)] for j in range(N)]
mas[0][0] = 1
if N > 2 and M > 1:
    mas[2][1] = 1
if M > 2 and N > 1:
    mas[1][2] = 1

for i in range(2, N):
    for j in range(2, M):
        mas[i][j] = mas[i-2][j-1]+mas[i-1][j-2]

print(mas[N-1][M-1])