#ABC408
# N, S = map(int, input().split())
# T = list(map(int, input().split()))

# prev = 0
# for t in T:
#     if t - prev > S+0.5:
#         print('No')
#         exit()
#     prev = t
# print('Yes')

N = int(input())
A = list(map(int, input().split()))

result = sorted(set(A))
print(len(result))
print(*result)