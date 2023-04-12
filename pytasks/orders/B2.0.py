n, m = [int(i) for i in input().split()]
#print(n, m) # количество общежитий и количество писем
mas = [int(i) for i in input().split()] # кол-ва квартир в общежитиях
#print(mas)
mas_let = [int(i) for i in input().split()] # номера квартир, куда направлены письма в порядке возрастания
#print(mas_let)

mas_new = []
sum = 0
for i in mas:
  sum = sum + i
  mas_new.append(sum)

#print(mas_new)
  
c = 0
for i in mas_let:
  prev = mas_new[c]
  while i > prev:
    if c < n - 1:
      c = c + 1
      prev = mas_new[c]
    else:
      break
  if c == 0:
    num = i
  else:
    num = i - mas_new[c-1]
  print(c+1, num)



