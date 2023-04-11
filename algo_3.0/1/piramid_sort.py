def func(heap, p, n):
    pos = p
    while (2*pos < n-2):
        if heap[pos] < max(heap[2*pos+1], heap[2*pos+2]):
            if heap[2*pos+1] < heap[2*pos+2]:
                heap[pos], heap[2*pos+2] =  heap[2*pos+2], heap[pos]
                pos = 2*pos+2
            else:
                heap[pos], heap[2*pos+1] =  heap[2*pos+1], heap[pos]
                pos = 2*pos+1
        else:
            break
    
N = int(input())
seq = list(map(int, input().split()))
for i in range((N//2)-1, -1, -1):
    seq.append(seq[i])
    func(seq, i, N+1)
    seq.pop()

for j in range(N-1):
    max_ = seq[0]
    seq[0] = seq[N-j-1]
    func(seq, 0, N-j)
    seq[N-j-1] = max_

print(*seq)