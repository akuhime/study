N = int(input())
seq = [1, 2, 4]
for L in range(2, N):
    seq.append(seq[L] + seq[L-1] + seq[L-2])
print(seq[N])