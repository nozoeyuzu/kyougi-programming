#ABC_397
# x = float(input())
# if x >= 38.0:
#     print(1)
# elif 37.5 <= x < 38.0:
#     print(2)
# else:
#     print(3)

S = list(input().strip())
ans = 0

if len(S)%2:
    ans +=1
for i in range(0,len(S)+1,2):
    if S[i] != 'i':
        ans += 1
for i in range(1,len(S), 2):
    if S[i] != 'o':
        ans += 1
print(ans)