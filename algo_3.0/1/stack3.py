N = int(input())
seq = list(map(int, input().split()))
stack = []
c = 1
while seq!=[]:
    k = seq.pop(0)
    if k!=c:
        stack.append(k)
    else:
        c+=1
        f = 1
        while f:
            try:
                a = stack.pop()
                if a!= c:
                    stack.append(a)
                    f = 0
                else:
                    c+=1
            except:
                f = 0 
    
if stack == sorted(stack, reverse=True):
    print('YES')
else:
    print('NO')