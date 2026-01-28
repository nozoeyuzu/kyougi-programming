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

# T = int(input())

# for _ in range(T):
#     N, W = map(int, input().split())
#     case = list(map(int, input().split()))
#     cost = [0] * (W*2)

#     for i in range(N):
#         cost[i%(2*W)] += case[i]
    
#     costs = cost + cost
#     c = sum(costs[0:W])
#     ans = c

#     for l in range(1, W*2):
#         c += costs[l + W -1] - costs[l - 1]
#         if c < ans:
#             ans = c
#     print(ans)

#TLEになった
# N = int(input())
# ans = []

# for i in range(1,N):
#     for j in range(i+1, N+1):
#         num = i**2 + j**2
#         if num <= N:
#             ans.append(num)
# print(len(ans))
# print(*sorted(ans))

# import math
# N = int(input())
# cnt = [0] * (N + 1)

# for i in range(1, math.isqrt(N)):
#     for j in range(i+1, math.isqrt(N-i*i) + 1):
#         num = i**2 + j**2
#         cnt[num] += 1
# ans = [n for n in range(1, N+1) if cnt[n] == 1]

# print(len(ans))
# print(*ans)

# N = int(input())
# A = list(map(int, input().split()))

# stack = []
# for x in A:
#     if stack and stack[-1][0] == x:
#         v, c = stack.pop()
#         c += 1
#         if c < 4:
#                 stack.append((v, c))
#     else:
#          stack.append((x, 1))

# ans = sum(c for _, c in stack)
# print(ans)

T = int(input())
for i in range(T):
    N = int(input())
    S = 0
    costs = []
    for _ in range(N):
        w, p = map(int, input().split()) 
        S += p
        costs.append(w+p)
    costs.sort()

    total = 0
    count = 0
    for c in costs:
        if total + c <= S:
            total += c
            count += 1
        else:
            break

    print(count)