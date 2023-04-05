from collections import deque


def simulate():
    def find_shark_pos():
        for i in range(n):
            for j in range(n):
                if space[i][j] == 9:
                    return i, j

    def bfs(shark_y, shark_x):
        delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
        visited_pos = set()
        q = deque()
        fish_to_eat_candi = list()
        dist = 0
        visited_pos.add((shark_y, shark_x))
        q.append((shark_y, shark_x))

        while q:
            q_size = len(q)
            dist += 1
            for _ in range(q_size):
                cy, cx = q.popleft()
                for dy, dx in delta:
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < n and 0 <= nx < n:
                        if space[ny][nx] > shark_size or (ny, nx) in visited_pos:
                            continue
                        else:
                            q.append((ny, nx))
                            visited_pos.add((ny, nx))
                            if space[ny][nx] < shark_size and space[ny][nx] != 0:
                                fish_to_eat_candi.append((dist, (ny, nx)))

            if len(fish_to_eat_candi) > 0:
                return fish_to_eat_candi

    n = int(input())
    space = [list(map(int, input().split())) for _ in range(n)]
    shark_y, shark_x = find_shark_pos()
    shark_size = 2
    eaten_fish_cnt = 0
    time = 0

    fish_to_eat_candi = bfs(shark_y, shark_x)
    while fish_to_eat_candi:
        fish_to_eat_candi.sort(key=lambda x: (x[0], x[1][0], x[1][1]))
        dist, fish_to_eat_pos = fish_to_eat_candi[0]
        space[shark_y][shark_x] = 0

        shark_y, shark_x = fish_to_eat_pos
        space[shark_y][shark_x] = 9
        time += dist
        eaten_fish_cnt += 1
        if eaten_fish_cnt == shark_size:
            shark_size += 1
            eaten_fish_cnt = 0

        fish_to_eat_candi = bfs(shark_y, shark_x)

    return time


print(simulate())
