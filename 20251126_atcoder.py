#ABC430
N,M = map(int, input().split())
S = [input().strip() for _ in range(N)]
seen = set()

for i in range(N-M+1):
    for j in range(N-M+1):
        row = ''
        block = []
        for di in range(M):
            for dj in range(M):
                row += S[i+di][j+dj]
        block.append(row)
        seen.add(tuple(block))
print(len(seen))
