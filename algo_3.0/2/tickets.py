c = float("inf")
seq = [[c for i in range(3)] for j in range(3)]
val = [0, 0, 0]
with open('input.txt', 'r') as f:
    N = int(f.readline())
    for i in range(3, N+3):
        seq.append(list(map(int, f.readline().split())))
        val.append(min(val[i-1]+seq[i][0], val[i-2]+seq[i-1][1], val[i-3]+seq[i-2][2]))
print(val[N+2])