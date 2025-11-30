#ABC432
# A, B, C = map(int, input().split())
# ans = []
# if A>B and A>C:
#     ans.append(A)
#     if B > C:
#         ans.append(B)
#         ans.append(C)
#     else:
#         ans.append(C)
#         ans.append(B)
# elif B>A and B>C:
#     ans.append(B)
#     if A > C:
#         ans.append(A)
#         ans.append(C)
#     else:
#         ans.append(C)
#         ans.append(A)
# else:
#     ans.append(C)
#     if A > B:
#         ans.append(A)
#         ans.append(B)
#     else:
#         ans.append(B)
#         ans.append(A)
# print(''.join(map(str,ans)))

# A,B,C = map(int, input().split())
# ans = sorted([A, B, C], reverse = True)
# print(''.join(map(str, ans)))

#0以外をソートして最後に最上位桁の後ろに0を挿入する。
# X = list(map(int, input().strip()))
# non_zero = [n for n in X if n!=0]
# zeros = [n for n in X if n==0]

# non_zero.sort()
# ans = non_zero[:1] + zeros + non_zero[1:]
# print(''.join(map(str,ans)))

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

if Y*min(A) < X*max(A):
    print(-1)
else:
    S = set()
    z = Y - X
    for i in range(N):
        S.add((X*A[i]) % z)
    if len(S) > 1:
        print(-1)
    else:
        g = Y*min(A)
        ans = 0
        for i in range(N):
            ans += (g - X * A[i]) // z
        print(ans)
