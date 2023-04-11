s = input().split()
stack = []
for i in s:
    try:
        stack.append(int(i))
    except:
        a, b = stack.pop(), stack.pop()
        stack.append(eval("{}{}{}".format(b, i, a)))
print(*stack)