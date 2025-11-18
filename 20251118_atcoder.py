#ABC_398
# N = int(input())
# result = ['-' for _ in range(N)]
# if N%2:
#     result[N//2] = '='
# else:
#     result[N//2-1] = '='
#     result[N//2] = '='
# print(''.join(result))

#異なる文字のカウントを複数保持する方法がパッと思いつかない
A = list(map(int, input().split()))
dictionary = dict()

for a in A:
    if a not in dictionary:
        dictionary[a] = 0
    dictionary[a] += 1

three_count = 0
two_count = 0
for v in dictionary.values():
    if v >= 3:
        three_count += 1
    if v >= 2:
        two_count += 1
if three_count >= 1 and two_count >=2:
    print('Yes')
else:
    print('No')
