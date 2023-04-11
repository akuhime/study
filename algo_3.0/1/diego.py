N = int(input())
seq = sorted(set(map(int, input().split())))
L = len(seq)
K = int(input())
seq2 = list(map(int, input().split()))
for i in seq2:
    l = L//2
    p = l
    res = -1
    while l>0:
        if seq[p] > f:
            p = l//2
            res = l
        else:
            p = l + l//2
        l = l//2
    print(res)
