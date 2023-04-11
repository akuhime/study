stack = []
dic = {'(':')', '{':'}', '[':']'}
s = input()
f = 1
for i in s:
    if i in ['(', '{', '[']:
        stack.append(i)
    else:
        try:
            a = stack.pop()
        except:
            print('no')
            f = 0
            break
        if i != dic[a]:
            print('no')
            f = 0
            break
        
if len(stack) == 0 and f:
    print('yes')
elif f:
    print('no')