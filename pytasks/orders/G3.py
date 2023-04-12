
from collections import deque

const_ = 2**30

n, k = [int(i) for i in input().split()]
dq = deque([int(i) for i in input().split()], n)
  
for i in range(k):
  x = dq[0]
  y = dq[n-1]
  if x < y:
    dq.popleft()
    if x+y < const_:
      dq.append(y+x)
    else:
      dq.append(y+x - const_)
  else:
    dq.pop()
    if x == y:
      dq.appendleft(0)
    else:
      dq.appendleft(y - x + const_)

for i in range(n):
  print(dq[i])


