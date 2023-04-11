
stack = []
f = 1
while f:
	s = input()
	match s:
		case 'size':
			print(len(stack))
		case 'clear':
			stack = []
			print('ok')
		case 'pop':
			if len(stack) == 0:
				print('error')
			else:
				print(stack.pop())
		case 'back':
			if len(stack) == 0:
				print('error')
			else:
				print(stack[-1])
		case 'exit':
			print('bye')
			f = 0
		case _:
			stack.append(int(s.split()[1]))
			print('ok')
