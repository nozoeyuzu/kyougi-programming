# N, K, X = map(int, input().split())
# A = list(map(int, input().split()))

# A.sort()
# prefix = [0] * (N+1)

# for i in range(N):
#     prefix[i+1] = prefix[i] + A[i]

# if prefix[K] < X:
#     print(-1)

# for m in range(N-K+1, N+1):
#     t = m + K - N
#     l = N - m
#     r = N - m + t
#     sake_min = prefix[r] - prefix[l]

#     if sake_min >= X:
#         print(m)
#         exit()

T = int(input())

for _ in range(T):
    N, W = map(int, input().split())
    case = list(map(int, input().split()))
    cost = [0] * (W*2)

    for i in range(N):
        cost[i%(2*W)] += case[i]
    
    costs = cost + cost
    c = sum(costs[0:W])
    ans = c

    for l in range(1, W*2):
        c += costs[l + W -1] - costs[l - 1]
        if c < ans:
            ans = c
    print(ans)
