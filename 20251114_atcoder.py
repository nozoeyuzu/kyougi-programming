#ABC_400
# A = int(input())
# if 400 % A == 0:
#     print(400//A)
# else:
#     print(-1)

# N, M = map(int, input().split())
# ans = 0
# for i in range(M+1):
#     ans += N**i
#     if ans > 1000000000:
#         print('inf')
#         exit()
# print(ans)

#ABC_399
# N = int(input())
# S = list(input().strip())
# T = list(input().strip())
# count = 0

# for i in range(N):
#     if S[i] != T[i]:
#         count+=1
# print(count)

N = int(input())
P = list(map(int,input().split()))
for i in range(N):
    r = 1
    for j in range(N):
        if P[j] > P[i]:
            r += 1
    print(r)

