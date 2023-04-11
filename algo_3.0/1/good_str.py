N = int(input())
a = int(input())
s = 0
for i in range(N-1):
    b = int(input())
    s += min(a,b)
    a = b
print(s)