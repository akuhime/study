from collections import deque
from datetime import datetime
import math
const_ = 2**30

def func2(n, k):

  dq = deque([int(n - i) for i in range(0, n)], n+1)
  start_time2 = datetime.now()
  for i in range(k):
    x = dq[0]
    y = dq[n-1]
    if x < y:
      dq.popleft()
      dq.append((y+x) & 0x7FFFFFFF)
    else:
      dq.pop()
      dq.appendleft(y - x + const_)

    #print(dq)

  print(dq)

  time2 = (datetime.now() - start_time2)
  print(time2)

func2(30000,100000000)
