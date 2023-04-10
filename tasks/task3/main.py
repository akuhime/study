n, k = map(int, input().split())
newborn = 1
adult = 0
for i in range(1, n):
    newborn_new_value = adult*k 
    adult = adult + newborn 
    newborn = newborn_new_value
print(newborn+adult)