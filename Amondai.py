# X, Y, Z = map(int, input().split())

# for i in range(1000):
#     if (X+i) == Z * (Y+i):
#         print('Yes')
#         exit()
# print('No')

W, B = map(int, input().split())
print(W*1000//B+1)