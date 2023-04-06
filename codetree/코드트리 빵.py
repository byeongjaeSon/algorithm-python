from collections import deque

# 격자 크기, 사람 수
n, m = map(int, input().split())

# board[i][j] = 1 or 0 : 베이스 캠프인지 아닌지
board = [list(map(int, input().split())) for _ in range(n)]

# i번째 사람이 가고싶어하는 편의점 위치 (y, x)
wanted_store_pos = [0] * m
for i in range(m):
    y, x = map(int, input().split())
    wanted_store_pos[i] = (y-1, x-1)

# 이미 점령당해 갈 수 없는 편의점 또는 베이스 캠프 위치
cant_visit_pos = set()

# 현재 시각
time = 1

# 이동 방향 위쪽 왼쪽 오른쪽 아래쪽 방향 순 (최단 거리 이동시 우선순위)
delta = ((-1, 0), (0, -1), (0, 1), (1, 0))

# 아직 편의점에 도착하지 못한 격자 안에 있는 사람들의 번호
left_person = set()

# 사람들의 위치
positions = [0] * m


def get_shortest_dist(cant_visit_pos, person_num, start_y, start_x):
    dest_y, dest_x = wanted_store_pos[person_num]
    q = deque([(start_y, start_x)])
    visited_pos = { (start_y, start_x) }
    level = 1

    if start_y == dest_y and start_x == dest_x:
        return 0

    while q:
        q_size = len(q)
        for _ in range(q_size):
            cy, cx = q.popleft()
            for dy, dx in delta:
                ny, nx = cy + dy, cx + dx
                # 최단거리 반환
                if ny == dest_y and nx == dest_x:
                    return level

                # 이미 방문한 곳인지 범위 밖인지 체크
                if ny < 0 or ny >= n or nx < 0 or nx >= n or (ny, nx) in visited_pos:
                    continue

                # 점령당한 위치인지 체크
                if (ny, nx) in cant_visit_pos:
                    continue

                q.append((ny, nx))
                visited_pos.add((ny, nx))

        level += 1

    return float('inf')


def move_forward_store(cant_visit_pos, left_person, positions):
    for person_num in left_person:
        # BFS 이용하여 가고싶은 편의점까지 최단 거리를 찾는다.
        cy, cx = positions[person_num]
        direction_to_distance = [0] * 4
        for i, (dy, dx) in enumerate(delta):
            ny, nx = cy + dy, cx + dx
            # 상하좌우 별 편의점까지 최단 거리가 나옴.
            direction_to_distance[i] = get_shortest_dist(cant_visit_pos, person_num, ny, nx)

        # 최단거리로 움직이며 최단 거리로 움직이는 방법이 여러가지라면 ↑, ←, →, ↓ 의 우선 순위로 움직이게 됩니다.
        min_distance = min(direction_to_distance)
        for i, dist in enumerate(direction_to_distance):
            if dist == min_distance:
                ny = cy + delta[i][0]
                nx = cx + delta[i][1]
                # 최단거리로 이동할 때 사람들의 위치 갱신
                positions[person_num] = (ny, nx)


def check_arrive_store(positions, cant_visit_pos, left_person):
    # 갱신된 사람들의 위치로 편의점 도착여부 판단
    arrived_person = list()
    for person_num in left_person:
        if positions[person_num] == wanted_store_pos[person_num]:
            cant_visit_pos.add(positions[person_num])
            arrived_person.append(person_num)

    for person_num in arrived_person:
        left_person.discard(person_num)

def find_nearest_basecamp_pos(board, start_y, start_x, cant_visit_pos):
    q = deque([(start_y, start_x)])
    visited_pos = {(start_y, start_x)}
    basecamp_candi = list()
    while q:
        q_size = len(q)
        for _ in range(q_size):
            cy, cx = q.popleft()
            for dy, dx in delta:
                ny, nx = cy + dy, cx + dx

                # 이미 방문한 곳인지 범위 밖인지 체크
                if ny < 0 or ny >= n or nx < 0 or nx >= n or (ny, nx) in visited_pos:
                    continue

                # 점령당한 위치인지 체크
                if (ny, nx) in cant_visit_pos:
                    continue

                # 가장가까운(최단거리)의 베이스 캠프를 찾았으므로 위치 반환
                if board[ny][nx] == 1:
                    basecamp_candi.append((ny, nx))

                q.append((ny, nx))
                visited_pos.add((ny, nx))

        if basecamp_candi:
            return basecamp_candi
    return -1

def move_to_basecamp(board, person_num, positions, wanted_store_pos, cant_visit_pos, left_person):
    start_y, start = wanted_store_pos[person_num]
    basecamp_candi = find_nearest_basecamp_pos(board, start_y, start, cant_visit_pos)
    basecamp_candi.sort(key = lambda x : (x[0], x[1]))
    basecamp_y, basecamp_x = basecamp_candi[0]
    cant_visit_pos.add((basecamp_y, basecamp_x))
    positions[person_num] = (basecamp_y, basecamp_x)
    left_person.add(person_num)

while True:
    # 격자에 있는 사람들이 편의점을 향해 최단거리 방향으로 1칸 움직임
    move_forward_store(cant_visit_pos, left_person, positions)

    # 편의점 도착여부 확인 및 cant_visit_pos 추가, left_person 삭제
    check_arrive_store(positions, cant_visit_pos, left_person)

    # t <= m 일 경우 t번 사람이 편의점에 가까우며
    # cant_visit_pos에 위치하지 않은 베이스 캠프로 이동 -> 격자 안으로 들어옴.
    # 여러 가지인 경우에는 그 중 행이 작은 베이스캠프, 행이 같다면 열이 작은 베이스 캠프
    if time <= m:
        person_num = time-1
        move_to_basecamp(board, person_num, positions, wanted_store_pos, cant_visit_pos, left_person)

    if not left_person:
        break

    time += 1

print(time)