N = int(input())
seq = list(map(int, input().split()))
res = [-1 for i in range(N)]
stack = []
for i in range(N):
    f = 1
    while f:
        try:
            a = stack.pop()
            if seq[i] >= a[1]:
                stack.append(a)
                f = 0
            else:
                res[a[0]] = i 
        except:
            f = 0
    stack.append((i, seq[i]))
print(*res)