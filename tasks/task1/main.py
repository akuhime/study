# минимальное, среднее и максимальное время
import re
import math
with open('pink.txt', 'r') as file:
    mas = file.readlines()
    sum = 0
    max = 0
    min = 1000
    for i in mas:
        time = int(re.search('\d+', str(re.search('время=\d*', i)[0]))[0])
        sum = sum + time
        if max < time: max = time
        if min > time: min = time
    print(min, math.ceil(sum/len(mas)), max)