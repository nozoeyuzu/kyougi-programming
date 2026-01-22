N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
prefix = [0] * (N+1)

for i in range(N):
    prefix[i+1] = prefix[i] + A[i]

if prefix[K] < X:
    print(-1)

for m in range(N-K+1, N+1):
    t = m + K - N
    l = N - m
    r = N - m + t
    sake_min = prefix[r] - prefix[l]

    if sake_min >= X:
        print(m)
        exit()