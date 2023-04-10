import csv
import math
with open('pass.csv', 'r') as f:
  reader = csv.reader(f, delimiter=',')
  sum = 0
  cnt = 0
  for i in list(reader)[1:]:
    if i[5] != '':
        cnt = cnt+1
        sum = sum+float(i[5])
print(math.ceil(sum/cnt))