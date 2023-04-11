N = int(input())
K = int(input())
y = int(input())
x = int(input())
pP = y*2+x-2
var1 = pP+K
var2 = pP-K
b1 = (var1 <= N)
b2 = (var2 > 0)
if not b1 and not b2:
    print(-1)
elif b1 and not b2:
    print((var1+1)//2,2-(var1%2))
elif not b1 and b2:
    print((var2+1)//2,2-(var2%2))
else:
    if (y-(var2+1)//2) < ((var1+1)//2 - y):
        print((var2+1)//2,2-(var2%2))
    else:
        print((var1+1)//2,2-(var1%2))