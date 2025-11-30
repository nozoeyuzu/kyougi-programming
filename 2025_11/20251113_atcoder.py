#ABC_431
# H, B = map(int, input().split())
# if H > B:
#     print(H-B)
# else:
#     print(0)

X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())
weight = X
query = set()

for _ in range(Q):
    p = int(input())
    if p not in query:
        query.add(p)
        weight += W[p-1]
    elif p in query:
        query.remove(p)
        weight -= W[p-1]
    print(weight)
