import heapq

h = []

with open('heap.txt', 'r') as f:
    N = int(f.readline())
    for i in range(N):
        s = f.readline().rstrip('\n')
        if s == '1':
            print(heapq._heappop_max(h))
            # a = 1
        else:
            heapq.heappush(h, int(s.split()[1]))
            heapq._heapify_max(h)
            # a = 1