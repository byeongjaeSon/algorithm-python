import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

direction_to_positionDelta = {
    0: (-1, 0),  # 북
    1: (0, 1),  # 동
    2: (1, 0),  # 남
    3: (0, -1),  # 서
}
cleaned_room_cnt = 0
area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
is_clean = [[False] * m for _ in range(n)]
curr_pos, curr_direction = (r, c), d
nothing_to_do, need_to_clean = False, True
while True:
    if nothing_to_do:
        break

    # 1. 현재 위치를 청소한다.
    if need_to_clean and not is_clean[curr_pos[0]][curr_pos[1]]:
        is_clean[curr_pos[0]][curr_pos[1]] = True
        cleaned_room_cnt += 1
    else:
        need_to_clean = True

    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    for delta in range(1, 5):
        next_direction = (curr_direction - delta) % 4
        next_y, next_x = curr_pos[0] + direction_to_positionDelta[next_direction][0], curr_pos[1] + direction_to_positionDelta[next_direction][1]
        # 1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        if not is_clean[next_y][next_x] and area[next_y][next_x] != 1:
            curr_direction = next_direction
            curr_pos = (next_y, next_x)
            break
        # 2. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
        else:
            continue
    else:
        if curr_direction < 2:
            back_direction = curr_direction + 2
        else:
            back_direction = curr_direction - 2
        curr_pos = (curr_pos[0] + direction_to_positionDelta[back_direction][0], curr_pos[1] + direction_to_positionDelta[back_direction][1])
        # 4. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
        if area[curr_pos[0]][curr_pos[1]]:
            nothing_to_do = True
            break
        # 3. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
        else:
            need_to_clean = False

print(cleaned_room_cnt)
