import copy
n = int(input())
mas = list(map(float, input().split()))
mas_fit = copy.deepcopy(mas)
for i in range(1,n-1):
    mas_fit[i] = (mas[i-1]+mas[i]+mas[i+1])/3
print (*["{0:0.7f}".format(i) for i in mas_fit])