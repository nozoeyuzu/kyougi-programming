#ABC431
# H, B = map(int, input().split())
# if H - B >= 0:
#     print(H-B)
# else:
#     print(0)

#取り付け済みを配列で管理するかブーリアンで管理するか
# X = int(input())
# N = int(input())
# W = list(map(int, input().split()))
# Q = int(input())
# flags = [False for _ in range(len(W))]
# weight = X

# for i in range(Q):
#     p = int(input())
#     if flags[p-1] == False:
#         weight += W[p-1]
#         flags[p-1] = True
#     else:
#         weight -= W[p-1]
#         flags[p-1] = False
#     print(weight)