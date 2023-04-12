n, k = [int(i) for i in input().split()]
mas = [int(i) for i in input().split()]
first = 0
last = n - 1
for i in range(k):
  x = mas[first]
  y = mas[last]
  if x < y:
    mas[first] = (y+x) % (2**30)
    first = (first + 1) % n
    last = (last + 1) % n
  else:
    mas[last] = (y-x) % (2**30)
    first = (first - 1) % n
    last = (last - 1) % n

for i in range(first, first+n):
  print(mas[i%n])


