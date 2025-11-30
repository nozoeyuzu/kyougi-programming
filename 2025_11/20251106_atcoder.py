# #ABC407
# A, B = map(int, input().split())
# print((A+B//2)//B)

# X, Y = map(int, input().split())
# count = 0
# for i in range(1, 7):
#     for j in range(1, 7):
#         if i+j >= X or abs(i-j) >= Y:
#             count += 1
# print(count/36)

#ABC406
# A,B,C,D = map(int, input().split())
# if C < A:
#     print('Yes')
# elif C == A and D <= B:
#     print('Yes')
# else:
#     print('No')

N, K = map(int, input().split())
A = list(map(int, input().split()))
result = 1
for i in range(N):
    if len(str(result*A[i])) > K:
        result = 1
    else:
        result = result*A[i]
print(result)
