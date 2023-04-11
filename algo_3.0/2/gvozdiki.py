N = int(input())
seq = sorted(list(map(int, input().split())))
diff = []
for i in range(N-1):
    diff.append(seq[i+1]-seq[i])
if N == 2:
    print(diff[0])
else:
    sum_ = [diff[0], diff[0]+diff[1]]
    for i in range(2,N-1):
        sum_.append(diff[i] + min(sum_[i-1], sum_[i-2]))
    print(sum_[N-2])

# pos = [0 for i in range(N-1)]
# res = []
# ans = 0
# for i in range(1,N-1):
#     if pos[i-1] == 0:
#         if abs(seq[i-1]-seq[i]) < abs(seq[i+1]-seq[i]):
#             pos[i-1] = 1
#             ans+= abs(seq[i-1]-seq[i])
#         else:
#             pos[i] = 1
#             ans+= abs(seq[i+1]-seq[i])
# if pos[N-2] == 0:
#     pos[N-2] == 1
#     ans+= abs(seq[N-1]-seq[N-2])

# print(ans)