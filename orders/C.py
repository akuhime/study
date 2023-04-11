n = int(input())
lst_ = []
len_ = len(lst_)
for i in range(n):
  req = input()
  if req == '-':
    if len_ == 1:
      print(-1)
    else:
      lst_.pop(0)
      len_ = len_ - 1
      min_ = min(lst_)
      print(min_)
  else:
    req = int(req.split()[1])
    lst_.append(req)
    if len_ == 0:
      min_ = req
    if req < min_:
      min_ = req
    len_ = len_ + 1
    print(min_)
  #print(lst_)

