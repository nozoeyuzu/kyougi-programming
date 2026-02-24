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

# N = int(input())
# S = input().strip()
# ans = 'o'*(N-len(S))+S
# print(ans)

# A, B = map(int, input().split())
# print(12*A + B)

# D, F = map(int, input().split())
# while(D>=F):
#     F += 7
# print(F-D)

# N = int(input())
# print(2**N - 2*N)

# X, Y = map(int, input().split())
# print(X*2**Y)

# P, Q = map(int, input().split())
# X, Y = map(int, input().split())

# if P <= X < P + 100 and Q <= Y < Q + 100:
#     print('Yes')
# else:
#     print('No')

# S = list(input().strip())
# cnt = 0

# for i in range(len(S)):
#     if S[i] == 'i' or S[i] == 'j':
#         cnt += 1
# print(cnt)

# S = input()
# print(S + 's')

N = list(input().strip())
if int(N[0]) == int(N[1]) == int(N[2]):
    print('Yes')
else:
    print('No')