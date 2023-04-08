from collections import deque


class Police:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.d_type = 0
        self.d = 0
        self.score = 0
        self.step = 0


class Criminal:
    def __init__(self, y, x, d_type):
        self.y = y
        self.x = x
        self.d_type = d_type
        self.d = 0


TREE = -1
POLICE = -2

police_delta = [[(-1, 0), (0, 1), (1, 0), (0, -1)], [(1, 0), (0, 1), (-1, 0), (0, -1)]]
criminal_delta = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]  # [우, 좌] [하, 상]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m, h, k = map(int, input().split())

# [] : 빈칸, 0~M-1 : 도망자, -1 : 나무, -2 : 술래
board = [[set() for _ in range(n)] for _ in range(n)]
sight_range = 3
police = Police(n // 2, n // 2)
board[n // 2][n // 2].add(POLICE)
criminals = []

turning_step = [deque(), deque()]


def init():
    # m개의 줄에 걸쳐 도망자의 위치 (y, x)와 이동 방법 d
    for criminal_num in range(m):
        y, x, d_type = map(int, input().split())
        # 이동 방법 d가 0인 경우 좌우로 움직임을, 1인 경우 상하로만 움직임
        # (zero-base로 변환)
        d_type -= 1
        y -= 1
        x -= 1
        criminals.append(Criminal(y, x, d_type))
        board[y][x].add(criminal_num)

    # h개의 줄에 걸쳐 나무의 위치 y, x
    for _ in range(h):
        y, x = map(int, input().split())
        y -= 1
        x -= 1
        board[y][x].add(TREE)

    for step in range(1, n):
        turning_step[0].append(step)
        turning_step[0].append(step)
    turning_step[0].append(n - 1)

    turning_step[1].append(n - 1)
    for step in range(n - 1, 0, -1):
        turning_step[1].append(step)
        turning_step[1].append(step)


def out_of_bound(y, x):
    return y < 0 or y >= n or x < 0 or x >= n


def find_move_criminals():
    move_criminal_candi = []
    for criminal_num in range(m):
        if criminals[criminal_num].y == -1:
            continue

        if abs(police.y - criminals[criminal_num].y) + abs(police.x - criminals[criminal_num].x) <= 3:
            move_criminal_candi.append(criminal_num)

    return move_criminal_candi


def move_criminals():
    # 도망자가 움직일 때 현재 술래와의 거리가 3 이하인 도망자만 움직입니다
    move_criminal_candi = find_move_criminals()

    for criminal_num in move_criminal_candi:
        cy, cx = criminals[criminal_num].y, criminals[criminal_num].x
        d_type, d = criminals[criminal_num].d_type, criminals[criminal_num].d
        dy, dx = criminal_delta[d_type][d]
        ny, nx = cy + dy, cx + dx

        # 현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나는 경우
        if out_of_bound(ny, nx):
            # 먼저 방향을 반대로 틀어줍니다.
            criminals[criminal_num].d = (criminals[criminal_num].d + 1) % 2

            # 이후 바라보고 있는 방향으로 1칸 움직인다 헀을 때 해당 위치에 술래가 없다면 1칸 앞으로 이동합니다.
            dy, dx = criminal_delta[d_type][criminals[criminal_num].d]
            ny, nx = cy + dy, cx + dx
            if POLICE not in board[ny][nx]:
                # 이동할 때는 항상 board와 crimials 동기화
                board[cy][cx].discard(criminal_num)
                board[ny][nx].add(criminal_num)

                criminals[criminal_num].y = ny
                criminals[criminal_num].x = nx
        # 현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나지 않는 경우
        else:
            # 움직이려는 칸에 술래가 있지 않다면 해당 칸으로 이동합니다. 해당 칸에 나무가 있어도 괜찮습니다.
            if POLICE not in board[ny][nx]:
                # 이동할 때는 항상 board와 criminals 동기화
                board[cy][cx].discard(criminal_num)
                board[ny][nx].add(criminal_num)

                criminals[criminal_num].y = ny
                criminals[criminal_num].x = nx


def is_turning_point():
    turning_step_cnt = turning_step[police.d_type].popleft()

    if turning_step_cnt == police.step:
        turning_step[police.d_type].append(turning_step_cnt)
        return True
    else:
        turning_step[police.d_type].appendleft(turning_step_cnt)
        return False


def move_police():
    # 위치 이동
    ## 격자와 경찰 모두 변경
    cy, cx = police.y, police.x
    dy, dx = police_delta[police.d_type][police.d]
    ny, nx = cy + dy, cx + dx

    board[cy][cx].discard(POLICE)
    board[ny][nx].add(POLICE)
    police.y = ny
    police.x = nx
    police.step += 1

    # 이동 후의 위치가 만약 이동방향이 틀어지는 지점이라면, 방향을 바로 틀어줍니다.
    if is_turning_point():
        police.d = (police.d + 1) % 4
        police.step = 0

    # 만약 이동을 통해 양끝에 해당하는 위치인 (1행, 1열) 혹은 정중앙에 도달하게 된다면 이 경우 역시 방향을 바로 틀어줘야 함에 유의합니다.
    if (ny, nx) == (0, 0):
        police.d_type = 1
        police.d = 0
    elif (ny, nx) == (n // 2, n // 2):
        police.d_type = 0
        police.d = 0


def catch_criminals():
    catched_criminal_cnt = 0
    dy, dx = police_delta[police.d_type][police.d]
    for s in range(sight_range):
        ny, nx = police.y + (dy * s), police.x + (dx * s)
        if out_of_bound(ny, nx):
            break

        if TREE in board[ny][nx]:
            continue

        catched_criminal = []
        for p in board[ny][nx]:
            if p >= 0:
                catched_criminal_cnt += 1
                catched_criminal.append(p)

        for criminal_num in catched_criminal:
            board[ny][nx].discard(criminal_num)
            criminals[criminal_num].y = -1
            criminals[criminal_num].x = -1

    return catched_criminal_cnt


def simulate(t):
    # m명의 도망자가 먼저 동시에 움직이고,
    move_criminals()

    # 그 다음 술래가 움직이고
    move_police()

    # 이동 직후 술래는 턴을 넘기기 전에 시야 내에 있는 도망자를 잡게 됩니다.
    catched_criminal_cnt = catch_criminals()
    police.score += t * catched_criminal_cnt


init()
for t in range(k):
    simulate(t + 1)

print(police.score)
