n = int(input())
lst_ = []
for i in range(n):
    name, num = input().split()
    num = int(num)
    lst_.append((name, num))
for i in sorted(lst_, key= lambda x: x[1]):
    print(i[0], i[1])