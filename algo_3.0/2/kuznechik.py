N, K = list(map(int, input().split()))
seq = [0 for j in range(K-1)]
seq.append(1)
for i in range(K, N+K-1):
    seq.append(sum(seq[i-K:i]))
print(seq[N+K-2])