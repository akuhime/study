N, M, K = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for i in range(N)]
for i in range(K):
    sum_ = 0
    x1, y1, x2, y2 = list(map(int, input().split()))
    for j in range(y1-1,y2):
        sum_ += sum(matrix[x1-1:x2][j])
    print(sum_)

