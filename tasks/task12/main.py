import csv
with open('data.csv', 'r') as f:
    sorted_data = sorted(list(csv.reader(f))[1:], key = lambda x: float(x[1]), reverse=True)
    print(sorted_data[0][0])
