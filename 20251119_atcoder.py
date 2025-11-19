#ABC_397
# x = float(input())
# if x >= 38.0:
#     print(1)
# elif 37.5 <= x < 38.0:
#     print(2)
# else:
#     print(3)

S = list(input().strip())
idx = 0
expected = 'i'
ans = 0

while idx < len(S):
    if S[idx] == expected:
        idx += 1
    else:
        ans += 1
    if expected == 'i':
        expected = 'o'
    else:
        expected = 'i'
if (ans + len(S)) % 2 == 1:
    ans += 1
print(ans)