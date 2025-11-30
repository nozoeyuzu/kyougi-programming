# #ABC_401
# S = int(input())
# if 200<= S <=299:
#     print('Success')
# else:
#     print('Failure')

N = int(input())
S = [input() for _ in range(N)]
login = False
error = 0
for s in S:
    if s == 'login':
        login = True
    elif s == 'logout':
        login = False
    elif s == 'public':
        pass
    elif s == 'private':
        if login == False:
            error += 1

print(error)