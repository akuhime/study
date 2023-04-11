lis = [list(map(int, input().split(':'))) for i in range(3)]
seclis = list(map(lambda x: x[0]*3600+x[1]*60+x[2],lis))
if seclis[2] < seclis[0]:
    seclis[2] += 24*3600
ans = seclis[1] + int((seclis[2]-seclis[0]+1)/2)
h = (ans//3600)%24
ans = ans%3600
m = ans//60
ans = ans%60
s = ans
print('{:02}'.format(h), ':', '{:02}'.format(m), ':', '{:02}'.format(s), sep='')