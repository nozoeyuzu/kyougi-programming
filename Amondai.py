# X, Y, Z = map(int, input().split())

# for i in range(1000):
#     if (X+i) == Z * (Y+i):
#         print('Yes')
#         exit()
# print('No')

# W, B = map(int, input().split())
# print(W*1000//B+1)

# N = int(input())
# sum = 0
# for i in range(N+1):
#     sum += i
# print(sum)

N = int(input())
S = input().strip()
ans = 'o'*(N-len(S))+S
print(ans)