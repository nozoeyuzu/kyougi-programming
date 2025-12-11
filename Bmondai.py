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

# N, M = map(int, input().split())
# ans = 0
# for i in range(M+1):
#     ans += N**i
#     if ans > 10**9:
#         print('inf')
#         exit()
# print(ans)

# N = int(input())
# error = 0
# login_flag = False

# for _ in range(N):
#     S = input()
#     if S == 'login':
#         login_flag = True
#     elif S == 'logout':
#         login_flag = False
#     if S == 'private' and login_flag == False:
#         error += 1
# print(error)

# Q = int(input())
# line = []
# for _ in range(Q):
#     query = list(map(int, input().split()))
#     if query[0] == 1:
#         line.append(query[1])
#     else:
#         print(line[0])
#         line.pop(0)

# T = list(map(str, input().strip()))
# U = list(map(str, input().strip()))

# for i in range(len(T)-len(U) + 1):
#     include = True
#     for j in range(len(U)):
#         if T[i+j] == U[j] or T[i+j] == '?':
#             continue
#         include = False
#     if include == True:
#         print('Yes')
#         exit()
# print('No')

# N = int(input())
# S = [input().strip() for _ in range(N)]
# T = [input().strip() for _ in range(N)]
# #0度,90度,180度,270度それぞれ回転させて、その状態で何回マスを置換したか計算
# new_S = S
# ans = 10**18

# def rotate(grid):
#     rotated = [[''] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             rotated[j][N - 1 - i] = grid[i][j]
#     return ["".join(row) for row in rotated]

# for r in range(4):
#     diff = 0
#     for i in range(N):
#         for j in range(N):
#             if new_S[i][j] != T[i][j]:
#                 diff += 1
#     ans = min(ans, r+diff)

#     new_S = rotate(new_S)
# print(ans)

# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# A_need = set([i for i in range(1,M+1)])
# ans = 0

# if not A_need.issubset(set(A)):
#     print(0)
#     exit()

# for i in range(N):
#     if A_need.issubset(A):
#         ans += 1
#     A.pop()

# print(ans)

# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# times = 1

# for i in range(N):
#     times = times * A[i]
#     if times >= 10**K:
#         times = 1
# print(times)

# X, Y = map(int, input().split())

# ans = set()
# for i in range(1, 7):
#     for j in range(1, 7):
#         if i+j >= X or abs(i-j) >= Y:
#             ans.add((i,j))
# print(len(ans)/36)

# N = int(input())
# A = list(map(int, input().split()))

# set_A = set(A)
# ans = sorted(set_A)
# print(len(ans))
# print(*ans)

# N = int(input())
# A = list(map(int, input().split()))
# ans = 0

# for i in range(N+1):
#     count = 0
#     for a in A:
#         if a >= i:
#             count += 1
#     if count >= i:
#         ans = i
    
# print(ans)

# N, Q = map(int, input().split())
# X = list(map(int, input().split()))
# count = [0 for _ in range(N)]
# ans = []

# for i in range(1, Q+1):
#     if X[i-1] != 0:
#         ans.append(X[i-1])
#         count[X[i-1]-1] += 1
#     else:
#         min_index = count.index(min(count))
#         ans.append(min_index+1)
#         count[min_index] += 1
# print(*ans)

# N = int(input())
# D = list(map(int, input().split()))

# for i in range(len(D)+1):
#     dist = 0
#     distance = []
#     for j in range(i+1, len(D)+1):
#         dist += D[j-1]
#         distance.append(dist)
#     print(*distance)

# S = list(input().strip())
# T = list(input().strip())

# for i in range(1, len(S)):
#     if S[i].isupper():
#         if S[i-1] in T:
#             continue
#         print('No')
#         exit()
#     continue
# print('Yes')

# N = int(input())
# S = [input().strip() for _ in range(N)]
# words = set()
# ans = 0

# for i in range(N):
#     for j in range(N):
#         if i==j:
#             continue
#         if S[i] + S[j] not in words:
#             words.add(S[i] + S[j])
#             ans += 1
# print(ans)

# N = int(input())
# S = [input().split() for _ in range(N)]
# ans = []
# word_count = 0
# for i in range(N):
#     S[i][1] = int(S[i][1])
#     word_count += S[i][1]
#     if word_count > 100:
#         print('Too Long')
#         exit()
#     S[i][1] = int(S[i][1])
#     ans.append(S[i][0]*S[i][1])
# print(''.join(ans))

# S = list(input().strip())
# ans = []
# for i in range(len(S)):
#     if S[i] == '#':
#         ans.append(i+1)
#     if len(ans) == 2:
#         print(','.join(map(str, ans)))
#         ans = []

S = list(input().strip())
T = []
o_flag = False

for i in range(len(S)):
    if S[i] == '#':
        T.append("#")
        o_flag = False
    elif S[i] == '.' and o_flag == False:
        T.append('o')
        o_flag = True
    else:
        T.append('.')
print(''.join(map(str,T)))
