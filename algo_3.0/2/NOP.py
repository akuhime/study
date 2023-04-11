with open('input.txt', 'r') as f:
    N = int(f.readline())
    seq1 = list(map(int, f.readline().split()))
    M = int(f.readline())
    seq2 = list(map(int, f.readline().split()))

mas = [[0 for i in range(N)] for j in range(M)]

a = seq1[0]
try:
    id_a = seq2.index(a)
except:
    id_a = -1

b = seq2[0]
try:
    id_b = seq1.index(b)
except:
    id_b = -1

if id_a != -1:
    for i in range(id_a, M):
        mas[i][0] = 1

if id_b != -1:
    for i in range(id_b, N):
        mas[0][i] = 1

for i in range(1, M):
    for j in range(1, N):
        if seq1[j] == seq2[i]:
            mas[i][j] = mas[i-1][j-1] + 1
        else:
            mas[i][j] = max(mas[i-1][j], mas[i][j-1])

x = M-1
y = N-1
res = []
while x >= 0 and y >= 0:
    if seq1[y] == seq2[x]:
        res.append(seq1[y])   
        x -= 1
        y -= 1
    else:
        if x == 0:
            y -= 1
        elif y == 0:
            x -= 1
        else:
            if mas[x-1][y] > mas[x][y-1]:
                x -= 1
            else:
                y -= 1 
       

print(*reversed(res))

 