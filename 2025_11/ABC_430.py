#A
# A, B, C, D = map(int, input().split())
# if A <= C and B <= D:
#     print('No')
# elif A <= C and B > D:
#     print('Yes')
# else:
#     print('No')

#B
# N, M = map(int, input().split())
# S = [input().strip() for _ in range(N)]
# seen = set()

# for i in range(N-M+1):
#     for j in range(N-M+1):
#         block = []
#         for di in range(M):
#             row = ''
#             for dj in range(M):
#                 row += S[i + di][j + dj]
#             block.append(row)
#         seen.add(tuple(block))
# print(len(seen))
