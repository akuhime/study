from random import randint 
ans = input()
N = 100000
doors_and_choises = [[randint(1,3), randint(1,3)] for i in range(N)]
win = 0
if ans == 'No':
    for i in doors_and_choises:
        if i[0] == i[1]:
            win += 1
else:
    for i in doors_and_choises:
        if i[0] != i[1]:
            win += 1
print('{:.2f}'.format(win/N))