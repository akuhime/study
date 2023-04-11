with open('queue.txt', 'r') as fi:
    queue = []
    f = 1
    while f:
        s = fi.readline().rstrip('\n')

        match s:
            case 'size':
                print(len(queue))
            case 'clear':
                queue = []
                print('ok')
            case 'pop':
                if len(queue) == 0:
                    print('error')
                else:
                    print(queue.pop(0))
            case 'front':
                if len(queue) == 0:
                    print('error')
                else:
                    print(queue[0])
            case 'exit':
                print('bye')
                f = 0
            case _:
                queue.append(int(s.split()[1]))
                print('ok')