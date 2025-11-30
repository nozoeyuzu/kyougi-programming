#ABC_404
# S = input().strip()
# set_S = set(S)

# for c in 'abcdefghijklmnopqrstuvwxyz':
#     if c not in set_S:
#         print(c)
#         exit()

N = int(input())
S = [input().strip() for _ in range(N)]
T = [input().strip() for _ in range(N)]

def diff_count(k: int) -> int:
    count = 0
    for i in range(N):
        rowT = T[i]
        for j in range(N):
            if k==0:
                si,sj = i,j
            elif k==1:
                si,sj = N-1-j, i
            elif k==2:
                si, sj = N - 1 - i, N - 1 - j
            else:
                si, sj = j, N - 1 - i
            
            if S[si][sj] != rowT[j]:
                count += 1
    return count

ans = 10**18
for k in range(4):
    flips = diff_count(k)
    rotations = k
    ans = min(ans, flips + rotations)

print(ans)