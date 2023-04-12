import csv
with open('data2.csv', 'r') as f:
    data = list(csv.reader(f))[1:]
    cnt = 0
    for i in data:
        if (i[3] == '4' and i[5] == 'Математика' and i[6] == 'победитель'): cnt += 1
    print(cnt)
