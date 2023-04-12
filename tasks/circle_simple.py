
def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def create_lst(n):
    lst1 = []
    i = 0
    while n > 0 :
        i = n%10
        lst1.append(i)
        n = n//10
       
    return lst1
    
def create_number(lst):
    n1 = 0
    n2 = 0
    n = 0
    lst2 = []
    while lst != []:
        n1 = lst.pop()
        lst2.append(n1)
        n = n*10 + n1
    while lst2 != []:
        n2 = lst2.pop()
        lst.append(n2)
    return n
    
def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    
def circle_number(n):
    lst = create_lst(n)
    t = 1
    for i in range(len(lst)):
        if isPrime(create_number(lst)) == 0 :
            t = 0
        shift(lst, 1)
    return t

def func(N):
    i = 0
    summ = 0
    while i < N:
        i = i + 1
        if circle_number(i):
            summ = summ + 1
            print(i)
    print("N = ")
    print(N)
    print("summ = ")
    print(summ)

func(1000000)


