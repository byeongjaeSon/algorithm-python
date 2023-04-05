import copy

board = [[0] * 4 for _ in range(4)]
directions = [0] * 16
positions = [0] * 16
delta = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
ret = 0

def init():
    for y in range(4):
        arr = list(map(int, input().split()))
        for i in range(0, 8, 2):
            x = i // 2
            a, b = arr[i] - 1, arr[i + 1] - 1
            board[y][x] = a
            directions[a] = b
            positions[a] = (y, x)


def solve(board, directions, positions, shark_y, shark_x, eaten_fish_cnt):
    temp_board = copy.deepcopy(board)
    temp_directions = copy.deepcopy(directions)
    temp_positions = copy.deepcopy(positions)

    # eat
    fish_num = temp_board[shark_y][shark_x]
    shark_direction = temp_directions[fish_num]
    temp_directions[fish_num] = -1
    temp_positions[fish_num] = -1
    temp_board[shark_y][shark_x] = -1

    global ret
    eaten_fish_cnt += (fish_num + 1)
    if ret < eaten_fish_cnt:
        ret = eaten_fish_cnt

    # fish move
    for fish_num in range(16):
        if temp_positions[fish_num] == -1:
            continue

        cy, cx = temp_positions[fish_num]
        for i in range(8):
            delta_idx = (temp_directions[fish_num] + i) % 8
            dy, dx = delta[delta_idx]
            ny, nx = cy + dy, cx + dx

            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4 or (ny == shark_y and nx == shark_x):
                continue

            if temp_board[ny][nx] == -1:
                temp_board[cy][cx], temp_board[ny][nx] = temp_board[ny][nx], temp_board[cy][cx]
                temp_positions[fish_num] = (ny, nx)
            else:
                temp_board[cy][cx], temp_board[ny][nx] = temp_board[ny][nx], temp_board[cy][cx]
                temp_positions[fish_num] = (ny, nx)
                temp_positions[temp_board[cy][cx]] = (cy, cx)

            temp_directions[fish_num] = delta_idx
            break

    # shark move
    for step in range(1, 4):
        ny = shark_y + delta[shark_direction][0] * step
        nx = shark_x + delta[shark_direction][1] * step
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            break

        if temp_board[ny][nx] != -1:
            solve(temp_board, temp_directions, temp_positions, ny, nx, eaten_fish_cnt)


init()
solve(board, directions, positions, 0, 0, 0)
print(ret)