#ABC_402
# S = input().strip()
# upper_list = []
# for s in S:
#     if s.isupper():
#         upper_list.append(s)
# print(''.join(upper_list))

# Q = int(input())
# query = [input().split() for _ in range(Q)]
# menu = []
# done = 0

# for i in range(Q):
#     if query[i][0] == '1':
#         menu.append(query[i][1])
#     else:
#         done += 1

# for i in range(done):
#     print((menu[i]))

Q = int(input())
query = [input().split() for _ in range(Q)]
menu = []
done = 0

for i in range(Q):
    if query[i][0] == '1':
        menu.append(query[i][1])
    else:
        print(menu[0])
        menu.pop(0)
