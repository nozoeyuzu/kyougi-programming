X, Y, Z = map(int, input().split())

for i in range(1000):
    if (X+i) == Z * (Y+i):
        print('Yes')
        exit()
print('No')
