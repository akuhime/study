with open('1/input1.txt','r') as f:
    N, M, K = list(map(int, f.readline().split()))
    matrix = [list(map(int, f.readline().split())) for i in range(N)]
    starts = []
    ends = []
    sums = []
    for i in matrix:
        starts.append([0] + [sum(i[0:j+1]) for j in range(0, M-1)])
        ends.append([sum(i[j:M]) for j in range(1, M)] + [0])
        sums.append(sum(i))
    #print(starts, ends,sums)
    for i in range(K):
        sum_ = 0
        x1, y1, x2, y2 = list(map(int, f.readline().split()))
        for j in range(x1-1,x2):
            #print(sums[j],starts[j][y1-1],ends[j][y2-1])
            sum_ += sums[j] - starts[j][y1-1] - ends[j][y2-1]
        print(sum_)
