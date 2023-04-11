heap = []
def func1():
    n = len(heap)
    pos = 0
    while (2*pos < n-2):
        if heap[pos] < max(heap[2*pos+1], heap[2*pos+2]):
            if heap[2*pos+1] < heap[2*pos+2]:
                heap[pos], heap[2*pos+2] =  heap[2*pos+2], heap[pos]
                pos = 2*pos+2
            else:
                heap[pos], heap[2*pos+1] =  heap[2*pos+1], heap[pos]
                pos = 2*pos+1
        else:
            break
def func2():
    n = len(heap)
    pos = n-1
    while (pos > 0):
        if heap[pos] >  heap[(pos-1)//2]:
            heap[pos], heap[(pos-1)//2] =  heap[(pos-1)//2], heap[pos]
            pos = (pos-1)//2
        else:
            break

with open('heap.txt', 'r') as f:
    N = int(f.readline())
    for i in range(N):
        s = f.readline().rstrip('\n')
        if s == '1':
            print(heap[0])
            heap[0] = heap[-1]
            func1()
            heap.pop()
        else:
            heap.append(int(s.split()[1]))
            func2()
