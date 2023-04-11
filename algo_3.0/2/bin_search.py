# найти первый элемент больше заданного в упорядоченном списке
from bisect import bisect_left
N = int(input())
seq = sorted(set(map(int, input().split())))
L = len(seq)
K = int(input())
seq2 = list(map(int, input().split()))
for i in seq2:
    print(bisect_left(seq, i))
print('ku')
for i in seq2:
    L = N
    s = 0 
    b = N-1
    while b!=s:
        if i > seq[L//2]:
            s = N//2
        else:
            b = N//2
    print()   