with open('1/input1.txt','r') as f:
    N, M, K = list(map(int, f.readline().split()))
    matrix = [list(map(int, f.readline().split())) for i in range(N)]

    s = 0
    prefix_sum_str = []
    for i in range(M):
        s+=matrix[0][i]
        prefix_sum_str.append(s)
    angles = [prefix_sum_str]
     
    for j in range(1, N):
        s = 0
        prefix_sum_str = []
        for i in range(M):
            s+=matrix[j][i]
            prefix_sum_str.append(s)
        angles.append([prefix_sum_str[k] + angles[j-1][k] for k in range(M)])

    for i in range(K):
        x1, y1, x2, y2 = list(map(int, f.readline().split()))
        if x1 == 1 and y1 == 1:
            sum_ = angles[x2-1][y2-1]
        elif x1 == 1:
            sum_ = angles[x2-1][y2-1] - angles[x2-1][y1-2]
        elif y1 == 1:
            sum_ = angles[x2-1][y2-1] - angles[x1-2][y2-1]
        else:
            sum_ = angles[x2-1][y2-1] - angles[x1-2][y2-1] - angles[x2-1][y1-2] + angles[x1-2][y1-2]
        print(sum_)
