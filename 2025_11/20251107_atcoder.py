#ABC405
# R, X = map(int, input().split())
# if X==1 and 1600<= R <= 2999:
#     print('Yes')
# elif X==2 and 1200<= R <= 2399:
#     print('Yes')
# else:
#     print('No')

# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = [i for i in range(1,M+1)]
# count = 0

# for i in range(N):
#     if B in A:
#         A.pop(len(A)-1)
#         count += 1
#     else:
#         print(count)
#         exit()
N, M = map(int, input().split())
A = list(map(int, input().split()))

need = set(range(1, M+1))
if not need.issubset(set(A)):
    print(0)
    exit()

first = {}
for i, x in enumerate(A):
    if x not in first:
        first[x] = i

ans = min(N - first[v] for v in range(1, M+1))
print(ans)
