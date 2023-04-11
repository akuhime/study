M = int(input())
N = int(input())
s = []
l = 0
for k in range(N):
    a, b =  list(map(int, input().split()))
    j = 0
    while j<l:
        i = s[j]
        if (b>=i[0]) and (a<=i[1]):
            s.pop(j)
            l-=1
        else:
            j+=1
    s.append((a,b))
    l += 1

print(l)