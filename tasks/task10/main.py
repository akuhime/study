def is_prime(n):
    if n==1: return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True
n = int(input())
sum = 0
cnt = 0
for i in range(2,n+1):
    if is_prime(i):
        sum += i
        cnt += 1
print('{:.2f}'.format(sum/cnt))
