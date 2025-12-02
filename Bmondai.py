# S = list(map(str, input().strip()))
# expected = 'i'
# position = 0
# ans = 0

# for _ in range(len(S)):
#     if S[position] == expected:
#         position += 1
#         if expected == 'i':
#             expected = 'o'
#         else:
#             expected = 'i'
#     else:
#         position += 1
#         ans += 1
# if (ans + len(S))%2:
#     ans += 1
# print(ans)

# A = list(map(int, input().split()))
# two_count = 0
# three_count = 0
# dictionary_A = {}

# for i in range(len(A)):
#     if A[i] not in dictionary_A:
#         dictionary_A[A[i]] = 0
#     dictionary_A[A[i]] += 1

# for v in dictionary_A.values():
#     if v >= 2:
#         two_count += 1
#     if v >= 3:
#         three_count += 1

# if three_count >= 1 and two_count >= 2:
#     print('Yes')
# else:
#     print('No')

# N = int(input())
# P = list(map(int, input().split()))
# k = [1] * N
# for i in range(N):
#     for j in range(N):
#         if P[i] < P[j]:
#             k[i] += 1
#     print(k[i])

N, M = map(int, input().split())
ans = 0
for i in range(M+1):
    ans += N**i
    if ans > 10**9:
        print('inf')
        exit()
print(ans)