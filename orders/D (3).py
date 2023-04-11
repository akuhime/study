from collections import Counter

n, k = [int(i) for i in input().split()]
lst_ = []
for i in range(n): 
  a = tuple([int(i) for i in input().split()])
  lst_.append(a)

lst_ = sorted(lst_, key=lambda x: (x[0], -x[1]), reverse = True)
#print(lst_)
              
cnt = Counter(lst_)
cnt = dict(cnt)
#print(cnt)

print(cnt[lst_[k-1]])


