n, m = map(int, input().split())
mas = [0 for i in range(m)]
mas[0] = 1
for i in range(1, n):
    newborn = sum(mas) - mas[0]
    for j in range(1, m):
        mas[m-j] = mas[m-1-j]
    mas[0] = newborn

print(sum(mas))


