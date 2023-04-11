from datetime import datetime
import time

n, k = [int(i) for i in input().split()]
#mas = [int(i) for i in input().split()]
mas = [int(n - i) for i in range(0, n)]

def func2():

  start_time2 = datetime.now()
  first = 0
  last = n - 1
  for i in range(k):
    #print('here cycle')
    if first == n:
      first = 0
    elif last == n:
      last = 0
    elif first == -1:
      first = n-1
    elif last == -1:
      last = n-1
    
    x = mas[first]
    y = mas[last]
    if x < y:
      mas[first] = (y+x) & (2**30 - 1)
      first = first + 1
      last = last + 1
    else:
      mas[last] = (y-x) & (2**30 - 1)
      first = first - 1
      last = last - 1

  print(mas[first:]+mas[:first])

  time2 = (datetime.now() - start_time2)
  print(time2)


func2()

