# #ABC412
# N = int(input())
# A = []
# B = []
# for _ in range(N):
#     a,b= map(int, input().split())
#     A.append(a)
#     B.append(b)
# count = 0
# for i in range(N):
#     if B[i] > A[i]:
#         count += 1

# print(count)

# S = input().strip()
# T = input().strip()

# for i in range(1, len(S)):
#     if S[i].isupper():
#         if S[i-1] not in T:
#             print('No')
#             exit()
# print('Yes')

#ABC411
# P = input().strip()
# L = int(input())

# if len(P) >= L:
#     print('Yes')
# else:
#     print('No')

N = int(input())
D = list(map(int, input().split()))
pos = [0]*N
for i in range(1,N):
    pos[i] = pos[i-1] + D[i-1]

for i in range(N-1):
    distance = []
    for j in range(i+1, N):
        distance.append(pos[j]-pos[i])
    print(*distance)