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

# T = int(input())
# for i in range(T):
#     N = int(input())
#     S = 0
#     costs = []
#     for _ in range(N):
#         w, p = map(int, input().split()) 
#         S += p
#         costs.append(w+p)
#     costs.sort()

#     total = 0
#     count = 0
#     for c in costs:
#         if total + c <= S:
#             total += c
#             count += 1
#         else:
#             break

#     print(count)

#MLE
# N, M = map(int, input().split())
# area = [[False]*(N+1) for _ in range(N+1)]
# count = 0
# for _ in range(M):
#     r, c = map(int, input().split())
#     block = [area[r][c], area[r+1][c], area[r][c+1], area[r+1][c+1]]
#     if any(block):
#         continue
#     else:
#         area[r][c] = True
#         area[r+1][c] = True
#         area[r][c+1] = True
#         area[r+1][c+1] = True
#         count += 1 
# print(count)

# N, M = map(int, input().split())
# block = set()
# count = 0
# for _ in range(M):
#     r, c = map(int, input().split())
#     if (r,c) not in block and (r+1,c) not in block and (r,c+1) not in block and (r+1,c+1) not in block:
#         block.add((r,c))
#         block.add((r+1,c))
#         block.add((r,c+1))
#         block.add((r+1,c+1))
#         count += 1
# print(count)

# N = int(input())
# A = list(map(int, input().split()))

# crr = 1 + A[0]

# for i in range(N):
#     if i+1 >= crr:
#         print(i)
#         exit()
#     crr = max(crr, i+1 + A[i])
# print(N)

T = int(input())
for _ in range(T):
    N, H = map(int, input().split())

    low = H
    high = H
    prev_t = 0
    ok = True

    for _ in range(N):
        t, l, u = map(int, input().split())
        dt = t - prev_t
        low -= dt
        high += dt
        low = max(low, 1)
        low = max(low, l)
        high = min(high, u)

        if low > high:
            ok = False
        prev_t = t

    print('Yes' if ok else 'No')
