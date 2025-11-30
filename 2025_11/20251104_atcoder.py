#ABC410
# N = int(input())
# A = list(map(int, input().split()))
# K = int(input())
# count = 0

# for i in range(N):
#     if A[i] >= K:
#         count += 1
# print(count)

N, Q = map(int, input().split())
X = list(map(int, input().split()))
count = [0]* N
ans = []

for i in range(Q):
    if X[i] >= 1:
        count[X[i]-1] += 1
        ans.append(X[i])
    else:
        m = min(count)
        for j in range(N):
            if count[j] == m:
                count[j] += 1
                ans.append(j+1)
                break
print(*ans)