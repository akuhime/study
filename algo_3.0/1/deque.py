deque = []
f = 1
while f:
    s = input()
    match s:
        case 'size':
            print(len(deque))
        case 'clear':
            deque = []
            print('ok')
        case 'pop_front':
            if len(deque) == 0:
                print('error')
            else:
                print(deque.pop(0))
        case 'pop_back':
            if len(deque) == 0:
                print('error')
            else:
                print(deque.pop())
        case 'front':
            if len(deque) == 0:
                print('error')
            else:
                print(deque[0])
        case 'back':
            if len(deque) == 0:
                print('error')
            else:
                print(deque[-1])
        case 'exit':
            print('bye')
            f = 0
        case _:
            s = s.split()
            if s[0] == 'push_front':
                deque = [int(s[1])] + deque
            else:
                deque.append(int(s[1]))
            print('ok')
