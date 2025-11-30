# import sys

# def main():
#     data = list(map(int, sys.stdin.read().split()))
#     ax1, ay1, bx1, by1, cx1, cy1, dx1, dy1, ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2 = data

#     x1 = [ax1, bx1, cx1, dx1]
#     y1 = [ay1, by1, cy1, dy1]
#     left1 = min(x1)
#     right1 = max(x1)
#     bottom1 = min(y1)
#     top1 = max(y1)

#     x2 = [ax2, bx2, cx2, dx2]
#     y2 = [ay2, by2, cy2, dy2]
#     left2 = min(x2)
#     right2 = max(x2)
#     bottom2 = min(y2)
#     top2 = max(y2)

#     if right1 < left2 or right2 < left1 or top1 < bottom2 or top2 < bottom1:
#         print('FALSE')
#     else:
#         print('TRUE')

# if __name__ == '__main__':
#     main()




# import sys

# def main():
#     input = sys.stdin.readline

#     n, m = map(int, input().split())
#     count = 0

#     follow = [[False] * (n + 1) for _ in range(n + 1)]

#     for _ in range(m):
#         a, b = map(int, input().split())
#         follow[a][b] = True


#     for a in range(1, n + 1):
#         for b in range(a + 1, n + 1):
#             for c in range(b + 1, n + 1):
#                 if follow[a][b] and follow[b][c] and follow[c][a] or follow[a][c] and follow[c][b] and follow[b][a]
#                     count += 1

#     print(count)

# if __name__ == "__main__":
#     main()
