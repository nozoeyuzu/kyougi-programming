#ABC_403
# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for i in range(N):
#     if i%2 == 0:
#         ans += A[i]
# print(ans)

T = list(input().strip())
U = list(input().strip())
ok = False
for i in range(len(T)-len(U)+1):
    match = True
    for j in range(len(U)):
        if T[i+j] != '?' and T[i+j] != U[j]:
            match = False
            break
    if match:
        ok = True
        break
print('Yes' if ok else "No")