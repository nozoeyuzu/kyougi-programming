S = list(map(str, input().strip()))
expected = 'i'
position = 0
ans = 0

for _ in range(len(S)):
    if S[position] == expected:
        position += 1
        if expected == 'i':
            expected = 'o'
        else:
            expected = 'i'
    else:
        position += 1
        ans += 1
if (ans + len(S))%2:
    ans += 1
print(ans)