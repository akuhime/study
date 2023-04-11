def func(a, b):
    if abs(b-a) == 9:
          return a < b
    return a > b
queue1 = list(map(int, input().split()))
queue2 = list(map(int, input().split()))
c = 0
while len(queue1)*len(queue2) !=0:
    c += 1
    a = queue1.pop(0)
    b = queue2.pop(0)
    if func(a,b):
        queue1.append(a)
        queue1.append(b)
    else:
        queue2.append(a)
        queue2.append(b)
if len(queue2) == 0:
    print('first', c)
else:
    print('second', c)

   