import csv
import math
with open('pass.csv', 'r') as f:
  reader = csv.reader(f, delimiter=',')
  sum1 = 0
  sum2 = 0
  sum3 = 0
  for i in list(reader)[1:]:
    if i[2] == '1':
        sum1 = sum1+1
    elif i[2] == '2':
        sum2 = sum2+1
    elif i[2] == '3':
        sum3 = sum3+1
print(sum1, sum2, sum3)