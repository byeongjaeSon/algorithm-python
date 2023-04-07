from collections import deque

# 격자의 크기 n, 팀의 개수 m, 라운드 수 k
n, m, k = map(int, input().split())
score_sum = 0
board = [list(map(int, input().split())) for _ in range(n)]
delta = ((-1, 0), (0, -1), (1, 0), (0, 1))


def out_of_bound(ny, nx):
    return ny < 0 or ny >= n or nx < 0 or nx >= n


def get_next_target_pos(curr_pos, visited_pos):
    for dy, dx in delta:
        ny, nx = curr_pos[0] + dy, curr_pos[1] + dx
        if out_of_bound(ny, nx):
            continue
        if (ny, nx) in visited_pos:
            continue
        if board[ny][nx] == 0:
            continue
        return ny, nx


def change_position(curr_pos, target_pos):
    board[curr_pos[0]][curr_pos[1]], board[target_pos[0]][target_pos[1]] = board[target_pos[0]][target_pos[1]], \
        board[curr_pos[0]][curr_pos[1]]


def get_src_pos(head_pos):
    for dy, dx in delta:
        ny, nx = head_pos[0] + dy, head_pos[1] + dx
        if out_of_bound(ny, nx):
            continue
        if board[ny][nx] != 2:
            continue

        return ny, nx


def move_toward_head(head_pos):
    src_pos = get_src_pos(head_pos)

    target_pos = -1
    curr_pos = src_pos

    for dy, dx in delta:
        ny, nx = src_pos[0] + dy, src_pos[1] + dx
        if out_of_bound(ny, nx):
            continue
        if board[ny][nx] == 1 or board[ny][nx] == 0:
            continue
        else:
            target_pos = (ny, nx)
            break

    visited_pos = set()
    while target_pos is not None:
        visited_pos.add(curr_pos)
        change_position(curr_pos, target_pos)
        curr_pos = target_pos
        target_pos = get_next_target_pos(curr_pos, visited_pos)


def move_forward():
    head_positions = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 1]
    for head_pos in head_positions:
        move_toward_head(head_pos)


def search_head_and_tail(hitted_pos):
    visited_pos = set()
    visited_pos.add(hitted_pos)
    q = deque([hitted_pos])
    head_pos, tail_pos = -1, -1

    while q:
        cy, cx = q.popleft()

        if board[cy][cx] == 1:
            head_pos = (cy, cx)

        if board[cy][cx] == 3:
            tail_pos = (cy, cx)

        if head_pos != -1 and tail_pos != -1:
            return head_pos, tail_pos

        for dy, dx in delta:
            ny, nx = cy + dy, cx + dx
            if out_of_bound(ny, nx) or (ny, nx) in visited_pos:
                continue
            if board[ny][nx] == 0:
                continue

            visited_pos.add((ny, nx))
            q.append((ny, nx))

    return -1, -1


def dfs(hitted_pos, curr_pos, visited_pos):
    if hitted_pos == curr_pos:
        return 1
    cy, cx = curr_pos
    for dy, dx in delta:
        ny, nx = cy + dy, cx + dx
        if (ny, nx) in visited_pos or out_of_bound(ny, nx) or board[ny][nx] == 0:
            continue
        visited_pos.add(curr_pos)
        next_pos = (ny, nx)
        return 1 + dfs(hitted_pos, next_pos, visited_pos)


def calc_dist(head_pos, hitted_pos):
    if head_pos == hitted_pos:
        return 1

    visited_pos = set()
    visited_pos.add(head_pos)
    curr_pos = get_src_pos(head_pos)

    return 1 + dfs(hitted_pos, curr_pos, visited_pos)


def throw_ball(round):
    index = (round // n) % 4
    alpha = round % n if index < 2 else (n - 1) - (round % n)
    hitted_pos = -1

    if index == 0:
        for x in range(n):
            if board[alpha][x] == 0 or board[alpha][x] == 4:
                continue
            hitted_pos = (alpha, x)
            break
    elif index == 1:
        for y in range(n - 1, -1, -1):
            if board[y][alpha] == 0 or board[y][alpha] == 4:
                continue
            hitted_pos = (y, alpha)
            break
    elif index == 2:
        for x in range(n - 1, -1, -1):
            if board[alpha][x] == 0 or board[alpha][x] == 4:
                continue
            hitted_pos = (alpha, x)
            break
    else:
        for y in range(n):
            if board[y][alpha] == 0 or board[y][alpha] == 4:
                continue
            hitted_pos = (y, alpha)
            break

    if hitted_pos == -1:
        return 0, 0, 0

    head_pos, tail_pos = search_head_and_tail(hitted_pos)
    dist = calc_dist(head_pos, hitted_pos)

    return dist, head_pos, tail_pos


def simulate(round):
    # 1. 먼저 각 팀은 머리사람을 따라서 한 칸 이동합니다.
    move_forward()

    # 2. 각 라운드마다 공이 정해진 선을 따라 던져집니다.
    dist, head_pos, tail_pos = throw_ball(round)
    # 공을 획득한 팀의 경우에는 머리사람과 꼬리사람이 바뀝니다. 즉 방향을 바꾸게 됩니다.
    if dist > 0:
        change_position(head_pos, tail_pos)

    return dist * dist


for round in range(k):
    score_sum += simulate(round)

print(score_sum)
