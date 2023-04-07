# 격자의 크기 n, 박멸이 진행되는 년 수 m, 제초제의 확산 범위 k, 제초제가 남아있는 년 수 c
n, m, k, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
killer = [[0 for _ in range(n)] for _ in range(n)]
killer_delta = ((-1, -1), (-1, 1), (1, -1), (1, 1))
tree_delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
total_died_tree_cnt = 0


def out_of_bound(y, x):
    return y < 0 or y >= n or x < 0 or x >= n


def calc_nearby_tree(i, j):
    nearby_tree_cnt = 0
    for dy, dx in tree_delta:
        ny, nx = i + dy, j + dx
        if out_of_bound(ny, nx):
            continue
        if board[ny][nx] >= 1:
            nearby_tree_cnt += 1
    return nearby_tree_cnt


def grow_tree():
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 1:
                nearby_tree_cnt = calc_nearby_tree(i, j)
                board[i][j] += nearby_tree_cnt


def get_nearby_empty_cell(i, j):
    empty_cell_pos = []
    for dy, dx in tree_delta:
        ny, nx = i + dy, j + dx
        if out_of_bound(ny, nx) or killer[ny][nx] >= 1:
            continue
        if board[ny][nx] == 0:
            empty_cell_pos.append((ny, nx))

    return empty_cell_pos


def spread_tree():
    temp_board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 1:
                empty_cell_pos = get_nearby_empty_cell(i, j)
                if len(empty_cell_pos) == 0:
                    continue
                new_tree_cnt = board[i][j] // len(empty_cell_pos)
                for empty_cell in empty_cell_pos:
                    temp_board[empty_cell[0]][empty_cell[1]] += new_tree_cnt

    for i in range(n):
        for j in range(n):
            board[i][j] += temp_board[i][j]


def calc_died_tree(i, j):
    died_tree_cnt = board[i][j]
    for dy, dx in killer_delta:
        for step in range(1, k + 1):
            ny, nx = i + (dy * step), j + (dx * step)
            if out_of_bound(ny, nx) or board[ny][nx] == -1 or board[ny][nx] == 0:
                break
            died_tree_cnt += board[ny][nx]
    return died_tree_cnt


def kill_tree(killer_pos):
    killer_y, killer_x = killer_pos
    board[killer_y][killer_x] = 0
    killer[killer_y][killer_x] = c

    for dy, dx in killer_delta:
        for step in range(1, k + 1):
            ny, nx = killer_y + (dy * step), killer_x + (dx * step)
            if out_of_bound(ny, nx):
                break

            # 단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
            if board[ny][nx] == -1 or board[ny][nx] == 0:
                killer[ny][nx] = c
                break

            killer[ny][nx] = c
            board[ny][nx] = 0


def spray_killer():
    max_died_tree_cnt = 0
    killer_pos = (-1, -1)
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 1:
                died_tree_cnt = calc_died_tree(i, j)
                if died_tree_cnt > max_died_tree_cnt:
                    killer_pos = (i, j)
                    max_died_tree_cnt = died_tree_cnt

    return max_died_tree_cnt, killer_pos


def killer_life_count_down():
    for i in range(n):
        for j in range(n):
            if killer[i][j] >= 1:
                killer[i][j] -= 1

for year in range(m):
    # 1. 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다. 성장은 모든 나무에게 동시에 일어납니다.
    grow_tree()

    # 2. 기존에 있었던 나무들은 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식을 진행합니다.
    # 이때 각 칸의 나무 그루 수에서 총 번식이 가능한 칸의 개수만큼 나누어진 그루 수만큼 번식이 되며,
    # 나눌 때 생기는 나머지는 버립니다. 번식의 과정은 모든 나무에서 동시에 일어나게 됩니다.
    spread_tree()

    # 3. 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다.
    died_tree_cnt, killer_pos = spray_killer()
    total_died_tree_cnt += died_tree_cnt

    if year > 0:
        killer_life_count_down()

    if died_tree_cnt > 0:
        kill_tree(killer_pos)
    else:
        killer[0][0] = c

print(total_died_tree_cnt)
