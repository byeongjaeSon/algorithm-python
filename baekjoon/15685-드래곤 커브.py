import sys
import copy

delta = ((0, 1), (-1, 0), (0, -1), (1, 0))
y_max = x_max = 101
board = [[False] * x_max for _ in range(y_max)]
n = int(sys.stdin.readline())
for _ in range(n):
    x, y, d, g = map(int, sys.stdin.readline().split())
    board[y][x] = True
    directions = [d]
    for _ in range(g):
        directions.extend(reversed(list(map(lambda x : (x+1)%4, copy.deepcopy(directions)))))

    for direction_idx in directions:
        dy, dx = delta[direction_idx]
        ny, nx = y + dy, x + dx
        board[ny][nx] = True
        y, x = ny, nx

cnt = 0
for y in range(100):
    for x in range(100):
        if board[y][x] and board[y+1][x] and board[y][x+1] and board[y+1][x+1]:
            cnt += 1

print(cnt)