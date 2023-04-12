def gen_fib(n):
    prev = 1
    cont = 1
    for i in range(1, n+1):
        if i == 1 or i == 2:
            yield 1
        else:
            next_ = prev + cont
            prev = cont
            cont = next_
            yield next_ 

generator = gen_fib(10)
print(*generator)